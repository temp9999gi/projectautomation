"""
The io module is in charge of loading and storing models.
It supports two file formats: XMI and a propietary format
based on the Python Pickle module.

The models can be retrieved and stored from a file, a url or the
repository.

The main functions are loadModel(name) and saveModel(name,model). 
These functions guess the file format and the backend based on the 
name parameter.

loadModels accepts a file name or url as a parameter.

Example:

 loadModel("test.xml") loads an XMI model from a local file.

 loadModel("test.smw") loads an SMW model from a local file.
 
 loadModel("smw://[<user[:<password>]@]<server>[:<portnumber>]/
           <repositoryname>[?tag=<branchname>][&revision=<revisionnumber>]
           [&sharedelement=<xmiid>]") retrieves a model from the repository.
           
 loadModel("smw://localhost/myproject?tag=Main")
 loadModel("smw://myuser:mypass@remoteserver/myproject?tag=Main")
 loadModel("smw://remoteserver/myproject?revision=134")
 loadModel("smw://remoteserver/myproject?revision=134&
                    sharedelement=ASharedPackage")
 loadModel("smw://remoteserver/myproject?revision=134&
                    sharedelement=DCE:5AAB77DE-DDE8-11D6-AFC7-0007468DDF7C")

Note that <xmiid> can be the the XMI id of an element for unambiguous
access to a specific element, or the "name" field of the element,
if it exists. In the latter case, the access could be ambiguous,
depending on the model and metamodel.

saveModel saves a complete model. The second parameter is any element
of the model, it does not need to be of type "Model". saveModel will
save the element passed as a parameter and everything transitively
connected to it, i.e. the whole model.

Example:

 saveModel("test.xml",myModel)
 will save myModel in the file test.xml, using the XMI format.

To Do:
 Add support for XMI 1.2

To Fix:
 + TaggedValues: problems with dataValue
 Maybe rootOwner should be a property of the metamodel
"""
try:
    from xml.dom import minidom
    import xml.dom
except:
    import sys
    print "An error ocurred while importing the xml modules"
    print "You need to install a Python XML package to be able to load and save XMI files"
    sys.exit(-1)

import codecs
import os
import urllib
import cPickle
import copy
import inspect
import types
import string
from smw.metamodel.MetaMM import *
from smw.metamodel.UniqueID import *
from smw import log
import StringIO
import re
from xml.sax.saxutils import quoteattr     
from smw import Configuration

__SMW_xmi_extender__ = "fi.abo.SMW"
__SMW_namespace__ = "SMW"

def nonEmptyString(s):
    for x in s:
        if x!=' ' and x!='\n' and x!='\r' and x!='\r\n':
            return 1
    return 0

### Model files

class XMIException(Exception):
    pass


def getDisplayUrl(url):
    """Removes the password from the url."""
    if url[:6] != "smw://":
        return url
    
    h = get_url_keys_and_values(url)
    if h.has_key("password"):
        del h["password"]
    display_url = create_url(h)
    return display_url

def __resolve_url__(url):
    assert(url[:6] == "smw://")
    url = url[6:]
    url = re.sub('\?.*', '', url)

    # Default username
    username = str(__config.getParameter("smw_client_default_username"))
    password = ""
    if url.find('@') != -1:
        # Username specified
        (username, url) = re.split('@', url, 1)
        if username.find(':') != -1:
            (username, password) = re.split(':', username, 1)

    (server, rest) = re.split('[:/]', url, 1)

    if rest.find("/") != -1:
        # Port specified
        (port, rest) = rest.split('/', 1)
    else:
        # Default port
        config = Configuration.Configuration()
        port = str(config.getParameter("smw_server_default_port"))

    # The rest is considered the repository name
    repository = rest

    return server, port, repository, username, password

def connect_to_server(url, authenticate = 1):
    """Connects to the server defined by the SMW URL string, created
    with create_url. If authenticate is set, tries to authenticate the
    user aswell. Usually needed, but some special case does not _immediately_
    require an authenticated connection (listing repositories, creating
    new repository). Note that the connection is
    currently NOT encrypted."""
    from smw.repository.smwclient import SMWClient
    # All this could be cached, especially the connection
    server, port, repository, username, password = __resolve_url__(url)
    server = server + ":" + port
    repserver = SMWClient("http://" + server)

    if authenticate:
        print "CONNECTING"
        print repserver.connect(repository, username, password)
        print repserver
        print "---"

    return repserver

def create_url(repkeys):
    """Returns an SMW URL string depending on the keys given.
    Valid keys are server, port, repository, user, password; these
    form the basis of the string. Additional options (after the ? sign)
    are _at least_ tag (which should be branch), revision, and sharedelement."""
    server = repkeys["server"]
    port = repkeys["port"]
    repository = repkeys["repository"]
    userpart = ""
    if repkeys.has_key("user") and len(repkeys["user"]) > 0:
        userpart = repkeys["user"]
        if repkeys.has_key("password") and len(repkeys["password"]) > 0:
            userpart += ":" + repkeys["password"]
        userpart += "@"

    addr = server + ":" + port
    
    t = "?"
    for i in repkeys.keys():
        if i == "user": continue
        if i == "password": continue
        if i == "addr": continue
        if i == "repository": continue
        if i == "server": continue
        if i == "port": continue
        if i == "savemodules": continue
        if i == "comment": continue
        # BUG escape them
        t += "%s=%s&" % (i, str(repkeys[i]))
    t = t[:-1] # chop
    # BUG escape them (except t)
    url = "smw://%s%s/%s%s" % (userpart, addr, repository, t)
    return url

def get_url_keys_and_values(url):
    h = {}
    if url.find('?') != -1:
        stuff = re.sub('.*\?', '', url)
        pairs = stuff.split('&');
        url = re.sub('\?.*', '', url)
    else:
        pairs = []

    for i in pairs:
        (key, value) = i.split('=')
        h[key] = value

    server, port, repository, username, password = __resolve_url__(url)
    h["server"] = server
    h["user"] = username
    h["password"] = password
    h["port"] = port
    h["repository"] = repository

    # Sane(?) defaults

    if not h.has_key("port"):
        # Default port
        config = Configuration.Configuration()
        h["port"] = str(config.getParameter("smw_server_default_port"))
    if not h.has_key("branch") and (not h.has_key("revision") or int(h["revision"]) == 0):
        # Default behaviour is to checkout main branch at latest
        h["branch"] = "Main"
    if not h.has_key("revision"):
        h["revision"] = "0"
    return h

def __load_xmi_url__(url, toupdate):
    r = connect_to_server(url)
    h = get_url_keys_and_values(url)
    if int(h["revision"]) == 0:
        rev = r.getLatestRevisionByBranchName(h["branch"])
    else:
        rev = h["revision"]
    if h.has_key("sharedelement"):
        (tagname, s, modules) = r.checkoutModel(rev, h["sharedelement"])
    else:
        (tagname, s, modules) = r.checkoutModel(rev)

    # Important!
    # This gives the information back to the GUI
    # what our new revision is.
    # Note that it must be done after a
    # successful checkout
    # Note that also module loading will set these keys
    # (the user is naturally free to ignore them)
    toupdate["revision"] = rev
    toupdate["branch"] = tagname
    return (StringIO.StringIO(s), modules)

def loadModel(url,metamodel=None, toupdate = None):
    """Loads a model. Valid supported protocols are:
       smw (proprietary XML-RPC lookalike)
       http
       ftp
       plain file.
       Supported filetypes are XMI and a proprietary
       Python pickled stream.
    """
    if toupdate == None:
        toupdate = {}
    modules = []
    if url[:6]=="smw://":
        (fd, modules) = __load_xmi_url__(url, toupdate)
        if fd.getvalue() == "":
            return None
    elif url[:7]=="http://"  or url[:6]=="ftp://":
        fd=urllib.urlopen(url)
    else:
        fd=open(url,"r")
    model=None
    try: 
        if url[-3:]!='xml'and url[-3:]!='xmi' and not url[:6] == "smw://":
            stmer=PickleStreamer(metamodel)
        else:
            stmer=XMIStreamer(metamodel)
        model=stmer.loadFromStream(fd)
    finally:
        fd.close()
    #
    # FIX THOSE DAMN MODULES
    #
    if modules:
        elements = getElementsOfModel(model)
        for (uuid, xmistring) in modules:
            if elements.has_key(uuid):
                elements[uuid].setModule(xmistring)

    return model

def loadModule(url, which_set):
    """Loads a module given by url and places it in the given set.
    E.g., for UML this could be mypackage.ownedElement."""

    h = get_url_keys_and_values(url)
    module = loadModel(url, None, h)
    #if h.has_key("branch"):
    #    del h["branch"]

    # Save the url string
    # It must be given to server at checkin
    h["sharedelement"] = module.__XMIid__()
    url = create_url(h)
    url = getDisplayUrl(url)

    module.setModule(url)

    #
    # ASSUME we can append it here. This doesn't work
    # for metamodels which have a maximum of one element
    which_set.append(module)

    return module

def updateModel(url, model, old_model, newversion = 0):
    """Updates the given model by the ModelDifference given by url.
    NOTE: Returns [possibly new] top-level model element,
    iff we have a new top-level element.
    Parameters:
    url   -- The url to get the difference from. Understands
             revision, module. ESPECIALLY not "branch", since we need
             a reference point, and the branch name is not usable.
    model -- Your model to patch
    old_model  -- The unmodified base model from the repository.
                  It is needed for proper diff3/patch3.
                  If none, we need to do a complete checkout and
                  the ModelDifference, instead of only the
                  ModelDifference.
    newversion -- Difference to what revision in the database, zero for
                  the newest
    NOTE: this is also used to update modules.
    """
    from smw.repository import diff
    from smw.repository import diff3
    server = connect_to_server(url)

    h = get_url_keys_and_values(url)

    print "OUR KEYS"
    print h

    revision = int(h["revision"])

    if newversion == 0:
        branch     = server.getBranchNameByRevision(revision)
        newversion = server.getLatestRevisionByBranchName(branch)

    # No update?
    if newversion == revision:
        return (model, old_model, revision)

    if not old_model:
        old_model = loadModel(url)
    
    canonified = server.diff(revision, newversion, h.get("sharedelement", 0))

    # this is the md that we can change, it is not applied to the
    # current model
    md = diff.ModelDifference(canonified)

    print "NEW MD TO BE APPLIED"
    print md

    new_pristine = modelcopy(old_model)
    md.patch(new_pristine)
    
    # user_md is already applied in the current diagram
    user_md = diff.ModelDifference(old_model, model)

    print "USER_MD"
    print user_md

    # Now, modify md according to user changes
    mergeconflicts = diff3.diff3(old_model, md, user_md)

    # Mergeconflicts?
    if mergeconflicts:
        print ""
        print "Conflicts found."
        print ""
        for i in mergeconflicts:
            print i
        print ""
        print "Resolve conflicts in md and then run md.patch3(model)"
        return (1, model, new_pristine, newversion, md, user_md)
    
    new_model = md.patch3(model)
    return (0, new_model, new_pristine, newversion)

def getHeader(url, toupdate = None):
    if toupdate == None:
        toupdate = {}
    if url[:6]=="smw://":
        (fd, modules) = __load_xmi_url__(url, toupdate)
        if fd.getvalue() == "":
            return None
    elif url[:7]=="http://"  or url[:6]=="ftp://":
        fd=urllib.urlopen(url)
    else:
        fd=open(url,"r")
    header=None
    try: 
        if url[-3:]!='xml' and url[-3:]!='xmi' and not url[:6] == "smw://":
            stmer=PickleStreamer()
        else:
            stmer=XMIStreamer()
        header=stmer.getHeader(fd)
    finally:
        fd.close()

    return header

def __save_xmi_url__(url, xmistring, toupdate):
    r = connect_to_server(url)
    h = get_url_keys_and_values(url)

    # Dangerous!
    #
    # Client will claim "hey, I'm the newest revision" even
    # though the revision could be anything
    #
    #if int(h["revision"]) == 0:
    #    rev = r.getLatestRevisionByBranchName(h["branch"])
    #else:
    #    rev = h["revision"]
    rev = h["revision"]

    if int(rev) == 0:
        rev = 1
    
    newtag = ""
    update = 1
    if h.has_key("newtag"):
        update = 0
        newtag = h["newtag"]

    print "SAVING"
    print xmistring, rev, newtag, toupdate.get("savemodules", None)
    print "comment", toupdate.get("comment", "<none given>")
    newrevision = r.checkinModel(xmistring, rev, newtag, toupdate["savemodules"], toupdate.get("comment", ""))
    #
    # Important!
    # This gives the information back to the GUI
    # what our new revision is.
    #
    toupdate["revision"] = newrevision
    print "IO",toupdate
    if not update and newtag:
        toupdate["branch"] = newtag
    
        
def saveModel(url,model, toupdate = None, profile=None):
    "Saves the model model in the given url"

    if toupdate == None:
        toupdate = {}
    
    assert(isinstance(model,MMClass))

    metamodel=inspect.getmodule(model.__class__)

    if url[:6]=="smw://":
        fd=StringIO.StringIO()
    else:
        fd=open(url,'wb')

    try:
        if url[-3:]!='xml' and url[-3]!='xmi' and not url[:6]=="smw://":
            stmer=PickleStreamer(metamodel)
        else:
            stmer=XMIStreamer(metamodel)
        stmer.saveToStream(model,fd,profile)
        if url[:6]=="smw://":
            #
            # FIX THOSE DAMN MODULES
            #
            savemodules = []
            elements = getElementsOfModel(model)
            for o in elements.keys():
                if elements[o].isModule():
                    savemodules.append((o, elements[o].getModule()))

            assert(not toupdate.has_key("savemodules"))
            toupdate["savemodules"] = savemodules
            __save_xmi_url__(url, fd.getvalue(), toupdate)
            del toupdate["savemodules"]
            
    finally:
        fd.close()
    return model
        
class ModelStreamer:
    def __init__(self,metamodel=None):
        self.metamodel=metamodel
        
    def setStrictMode(self,mode):
        self.strictMode=mode
        
    def loadFromStream(self,fd):
        raise "Not implemented"
    
    def saveToStream(self,model,fd,profile=None):
        raise "Not implemented"

    def getHeader(self,fd):
        return None

class PickleStreamer(ModelStreamer):

    def loadFromStream(self,fd):
        self.getHeader(fd)
        return cPickle.load(fd)

    def saveToStream(self,model,fd,profile=None):
        fd.write("SMW_MODEL\n")
        fd.write("METAMODEL "+model.getMetamodel().__name__+"\n")
        if not profile:
            profileName="None"
        else:
            profileName=str(profile.name)
        fd.write("PROFILE "+profileName+"\n")
        return cPickle.dump(model,fd)


    def getHeader(self,fd):
        signature=fd.readline()
        if not signature[:9]=="SMW_MODEL":
            #assert is too evil
            fd.seek(0)#"unread" first line
            return None
        metaspec=string.split(fd.readline())
        if len(metaspec)!=2:
            raise "Invalid metamodel specification",metaspec
        metamodel=metaspec[1]
        profilespec=string.split(fd.readline())
        if len(profilespec)!=2:
            raise "Invalid profile specification",profilespec
        profile=profilespec[1]
        return (metamodel,profile)

#
# XMI handling TODO, in ~priority order
# * xmi.extension, xmi.extensions (we need this for modules anyway)
# * is xmi.uuid ok now?
# * is xmi.label required? do we need to save it along with element?
# * other xmi header information, I guess we have to save them too?
# * href
# * xmi.idref can be relative
#


class XMIStreamer(ModelStreamer):
    def __init__(self,metamodel=None,strictMode=0,
                 rootOwner="ownedElement",generateParents=1):
        self.doc=None
        self.elementById={}
        self.objectById={}
        self.secondPass={}
        self.metamodel=metamodel
        self.strictMode=strictMode
        self.rootOwner=rootOwner
        self.headerFound=0
        self.generateParents=generateParents
        self.log=log.getLogger(self.__class__.__name__)
        
    def initializeMetamodel(self,name,version):
        modulename="smw.metamodel."+name+string.replace(version,'.','')
        module=None
        try:
            module=__import__(modulename,globals(),locals(),
                                 [string.split(modulename,'.')[-1]]
                                 )            
        except:
            if not self.metamodel:
                raise str("There is not metamodel module for "+name+" version "+version)

        if self.metamodel and self.metamodel!=module:
            if self.strictMode:
                raise "XMI file cannot be imported with metamodel "+ \
                      str(self.metamodel)
            else:
                self.log.warning("loading a model based on "+name+" version "+version+" with metamodel "+self.metamodel.MMFullName)
                    
                    
        else:
            self.metamodel=module
        
    def setRootOwner(self,rootOwner):
        assert(rootOwner and type(rootOwner)==type(""))
        self.rootOwner=rootOwner
        
    def findIds(self,node):
        if isinstance(node, xml.dom.minidom.Element):
            self.elementById[node.getAttribute('xmi.id').upper()]=node
            for c in node.childNodes:
                if c.nodeType!= xml.dom.Node.TEXT_NODE:
                    self.findIds(c)

    def saveToStream(self,model,fd,profile=None):
       ## if not model.__mm__.has_key(self.rootOwner):
##            raise "Model has not a rootOwner named "+self.rootOwner+":",model
##        if model.__mm__[self.rootOwner][0]==MMClass.kind__Association:
##            raise "Model rootOwner"+self.rootOwner+" is not an attribure or a composition:",model
        
        processed={}
        toProcess={}
        fd.write("<?xml version='1.0' encoding='ISO-8859-15'?>" + os.linesep)
        #fd.write("<!DOCTYPE XMI SYSTEM '"+self.metamodel.MMName+self.metamodel.MMVersion+".dtd' > " + os.linesep)
        fd.write("<XMI xmi.version='1.1' timestamp='" + time.strftime("%a, %d %b %Y %H:%M:%S %z") + "'>" + os.linesep)
        fd.write("<XMI.header>" + os.linesep)
        fd.write(" <XMI.metamodel xmi.name="+quoteattr(self.metamodel.MMName)+
                 " xmi.version='"+self.fromMMVersionToXMIVersion()+"'/>" + os.linesep)
        fd.write("</XMI.header>" + os.linesep)
        fd.write("<XMI.content>" + os.linesep)
        self.saveElement(model,fd,processed,toProcess,1,1)
        if 0:
            self.__saveDiagramInformation__(model, fd, 1)
        fd.write("</XMI.content>" + os.linesep)
        fd.write("</XMI>" + os.linesep)

    def __saveDiagramInformation__(self, model, fd, indent):
        from smw.diagraminterchange.xmidi import SaveXMIDI
        sxd = SaveXMIDI(fd)
        sxd.setIndent(indent)
        sxd.saveDiagrams(model.presentation)

    def fromMMVersionToXMIVersion(self):
        if len(self.metamodel.MMVersion)<2:
            return self.metamodel.MMVersion
        else:
            return self.metamodel.MMVersion[0]+"."+self.metamodel.MMVersion[1:]
    def fromXMIVersionToMMVersion(self,v):
        if len(v)<3:
            return v
        else:
            return v[0]+v[2:]
    
    def saveElement(self,element,fd,processed,toProcess,margin,inAggregation,context=''):
        if processed.has_key(element) or not inAggregation:
            if context:
                name=context
            else:
                name=element.__name__
            fd.write(" "*margin+"<"+self.metamodel.MMName+":"+name+ " xmi.idref='"+element.__XMIid__()+"'/>" + os.linesep)
            if not processed.has_key(element) and isinstance(element,Element):
                toProcess[element]=1
            return


        # We store xmi.uuid, the globally unique identification
        # Technically xmi.id is spurious, but xmi.idref can
        # only be used with xmi.id (?), and there is not
        # yet a definite XLink/XPointer standard for referencing
        # xmi.uuid:s!
        # 
        fd.write(" "*margin+"<"+self.metamodel.MMName+":"+element.__name__+ " xmi.id='"+element.__XMIid__()+"' xmi.uuid='"+element.__XMIid__()+"'")
        processed[element]=1
        if toProcess.has_key(element):
            del toProcess[element]
        aprocessed={}
        for a in element.__mm__.keys():
            if element.__mm__[a][2]==1:
                v=getattr(element,a)
                if v!=None:
                    # if it is an atomic value (a string or integer)
                    if type(v)!=types.InstanceType:                        
                        fd.write(" " +a+"="+quoteattr(element.__mm__[a][1]().toString(v)))
                        aprocessed[a]=1
                    # if it is an association
                    elif  element.__mm__[a][0]==MMClass.kind__Association:
                        fd.write(" " +a+"="+quoteattr(str(v.__XMIid__())))
                        aprocessed[a]=1
                        if not processed.has_key(v):
                            toProcess[v]=1

        fd.write(">" + os.linesep)

        #
        # SMW Extensions
        #
        if 1:
            #
            # Shared elements
            #
            if element.isModule():
                fd.write(" "*(margin+1) + "<XMI.extension xmi.extender=" + quoteattr(__SMW_xmi_extender__) + ">" + os.linesep)
                fd.write(" "*(margin+2) + "<" + __SMW_namespace__ + ":SharedElement uuid=" + quoteattr(str(element.__XMIid__())) + " xmistring=" + quoteattr(str(element.getModule())) + " />" + os.linesep)
                fd.write(" "*(margin+1) + "</XMI.extension>" + os.linesep)

        #
        # Other people's extensions here
        if 1 and element.xmiextension:
            for line in element.xmiextension:
                fd.write(" "*(margin+1) + line)
                
        
        # We should write
        #  1) Elements that have not been processed AND
        #  REMOVED: 2) are attributes or parts of a compositions AND
        #  3) are not presentations (XMI does not support them)

        for a in element.__mm__.keys():
            if not aprocessed.has_key(a) and \
                   element.__mm__[a][1].__name__!="PresentationElement":
                vlist=[]
                if element.__mm__[a][2]==1:
                    if getattr(element,a)!=None:
                        vlist=[getattr(element,a)]
                else:
                    vlist=getattr(element,a)
                print vlist,type(vlist)
                if len(vlist) or (
                    not context and a==self.rootOwner and \
                    len(toProcess.keys()) and self.generateParents):
                    base=element.__whereIsAttrDefined__(a).__name__
                    fd.write(" "*(margin+1)+"<"+self.metamodel.MMName+":"+ \
                             base+"."+a+">" + os.linesep)
                    for x in vlist:
                        self.saveElement(
                            x,fd,
                            processed,toProcess,
                            margin+2,
                            element.__mm__[a][0]!=MMClass.kind__Association,
                            element.__mm__[a][1].__name__)

                    if not context and a==self.rootOwner:
                        while len(toProcess.keys()):
                            self.saveElement(toProcess.keys()[0],fd,
                                             processed,toProcess,
                                             margin+2,
                                             element.__mm__[a][0]!=MMClass.kind__Association,
                                             element.__mm__[a][1].__name__)
                            
                    fd.write(" "*(margin+1)+"</"+self.metamodel.MMName+":"+base+"."+a+">" + os.linesep)
        fd.write(" "*margin+"</"+self.metamodel.MMName+":"+element.__name__+">" + os.linesep)
        
    def loadFromStream(self,fd):         
        self.elementById={}
        self.headerFound=0

        self.log.debug("Begin parsing XMI document...")
        self.doc=minidom.parse(fd)
        self.log.debug("Begin extracting model...")
        self.findIds(self.doc.documentElement)

        content= self.extractXMIContent(self.doc.documentElement)
        self.log.debug("Model extraction completed.")
        return content

    def __handleSMWExtension__(self, obj, node):
        # obj is the model element
        # node is the XMI.extension node
        for i in node.childNodes:
            if i.nodeType!= xml.dom.Node.TEXT_NODE:
                #
                # Shared element extension
                #
                print vars(i)
                if i.localName == __SMW_namespace__ + ":SharedElement":
                    obj.setModule(str(i.getAttribute("xmistring")))
    
    def extractAttributes(self,obj,node):
        namel=string.split(node.nodeName,'.')
        name=str(namel[-1])
        
        values=[]
        #
        # XMI.extension
        #
        if node.localName == "XMI.extension":

            # SMW extension?
            if node.getAttribute("xmi.extender") == __SMW_xmi_extender__:
                self.__handleSMWExtension__(obj, node)

            # other people's extensions
            else:
                if obj.xmiextension == None:
                    obj.xmiextension = []
                xmlstring = node.toprettyxml(indent=" ")
                for line in xmlstring:
                    obj.xmiextension.append(line)
            
            return
        
        if node.getAttribute("xmi.value")=="":
            for c in node.childNodes:
                if c.nodeType!= xml.dom.Node.TEXT_NODE:
                    values.append(self.extractElement(c))
                else:
                    if c.nodeValue and nonEmptyString(c.nodeValue):
                        values.append(str(c.nodeValue))
        else:
            values.append(node.getAttribute("xmi.value"))
            
        if len(values):
            if not obj.__mm__.has_key(name):
                if self.strictMode:
                    raise XMIException("Element "+str(obj)+" has no attribute "+name)
                else:
                    self.log.warning("Element "+str(obj)+" has no attribute "+name)
            else:
                try:
                    if obj.__mm__[name][2]==1:
                        v=values[0]
                        if type(v)==types.StringType or type(v)==types.UnicodeType:
                            try:
                                v=obj.__mm__[name][1]().fromString(v)
                            except:
                                # STUDY THIS
                                #print "(1)Warning: Cannot convert attribute",name,"value",v
                                pass

                        setattr(obj,name,v)
                    else:                          
                        for v in values:
                            #print v,values
                            if v and type(v)==types.InstanceType and isinstance(v,MMClass):
                                try:
                                    getattr(obj,name).append(v)
                                except WFRException,e:
                                    self.log.exception("Cannot set attribute obj=%s,attr=%s,value=%s" % (
                                        str(obj),str(name),str(v)))

                except WFRException,e:
                    if self.strictMode:
                        raise e
                    else:
                        self.log.info("Exception"+str(e)+" while setting attribute")

        
            
               
    def extractElement(self,node):
        # Has the node been processed already?

        if not isinstance(node, xml.dom.minidom.Element):
            return None
        
        # Cache these values for faster acces
        xmi_id = node.getAttribute('xmi.id').upper()
        xmi_idref = node.getAttribute('xmi.idref').upper()
        xmi_uuid = node.getAttribute('xmi.uuid').upper()
        
        # Is defined?
        if xmi_id:
            if self.objectById.has_key(xmi_id):
                return self.objectById[xmi_id]

        # Is a reference?
        if xmi_idref:
            if not self.objectById.has_key(xmi_idref):
                if not self.elementById.has_key(xmi_idref):
                    if self.strictMode:
                        raise WFRException("Node does not exist:",xmi_idref)
                    else:
                        self.log.warning("Malformed XMI file, Node does not exist:"+str(xmi_idref))
                        return None
                return self.extractElement(
                    self.elementById[xmi_idref])
            else:
                return self.objectById[xmi_idref]

        # The node has not been processed yet
        # We must create a new object for it

        if not xmi_uuid:
            # Create new ID, otherwise assume the given uuid
            # really is globally unique
            xmi_uuid = getUniqueID()
        
        name=node.nodeName

        t = self.metamodel.MMName + ":"
        if name[:len(t)]== t:
            # XMI 1.1 uses UML: as a prefix
            name=name[len(t):]
            
        # We are only interested in the name, not the full path
        namel=string.split(name,'.')
        name=str(namel[-1])

        if self.metamodel.__dict__.has_key(name):
            #print "creating a ",self.metamodel.__dict__[name]
            factory=self.metamodel.__dict__[name]
            if issubclass(factory,MMAtom):
                # Note, create it by xmi.uuid!
                obj=apply(factory,(),{'__uniqueID__':xmi_uuid})
                #assert(obj.__XMIid__() == xmi_uuid)
            else:
                obj=apply(factory,())
            #self.log.debug("Extracted object type %s with unique id %s" % (str(factory),str(obj.__uniqueID__)))
        else:
            if self.strictMode:
                raise WFRException("Metamodel "+self.metamodel.MMFullName+" does not contain element ",name)
            else:
                self.log.warning("Metamodel "+self.metamodel.MMFullName+" does not contain element "+str(name))
                obj=None

        if not hasattr(obj,"__mm__"):
            # It is a presentation
            obj=None

        # Save it by xmi_id, not by xmi_uuid
        # xmi_uuid uses XLink/XPointer
        self.objectById[xmi_id]=obj

        if not obj:
            return None

        # Process the attributes of the object
        
        # Process XMI 1.1  attributes
        for aname in obj.__mm__.keys():
            if obj.__mm__[aname][2]==1:
                v=node.getAttribute(aname)

                if v:
                    if type(v)==types.UnicodeType:
                        v=v.encode('iso-8859-15')
                    if type(v)==types.StringType:
                        try:
                            v=obj.__mm__[aname][1]().fromString(str(v))
                        except:
                            #Fix this 
                            #print "(2) Warning: Cannot convert attribute",name,"value",v
                            self.secondPass[(obj,aname)]=v.upper()
                            v=None
                if v:
                    #print "Setting attribute ",obj,aname+" to ",v
                    setattr(obj,aname,v)                   
        # Process XMI 1.0 and 1.1 attributes     
        for c in node.childNodes:
            if c.nodeType!= xml.dom.Node.TEXT_NODE:
                self.extractAttributes(obj,c)

        return obj
    
    def extractXMIContent(self,node):
        self.secondPass={}
        root=None
        if node.nodeName=='XMI':
            xmiVersion = node.getAttribute('xmi.version')
            metamodel = 'UML'
            if xmiVersion == '1.2':
                version = '1.4'
            else:
                version = '1.3'
            self.log.info("XMI metamodel %s infered from XMI version %s" % (version, xmiVersion))
            self.initializeMetamodel(metamodel,version)
        if node.nodeName=='XMI.header':
            if self.headerFound:
                self.log.info("XMI file has multiple headers! I will use the first one.")
            else:
                self.headerFound=1
                for c in node.childNodes:
                    if c.nodeName=="XMI.metamodel":
                        metamodel=c.getAttribute('xmi.name')
                        version=self.fromXMIVersionToMMVersion(c.getAttribute('xmi.version'))
                        self.log.info("XMI header found: metamodel %s version %s" % (metamodel,version))
                        self.initializeMetamodel(metamodel,version)
                        break
        if node.nodeName=='XMI.content':
            manyRoots=0
            for c in node.childNodes:
                if c.nodeType!= xml.dom.Node.TEXT_NODE and re.search("Model",c.nodeName,re.IGNORECASE):
                    if not root:
                        self.log.info("XMI root content found: extracting "+str(c.nodeName))
                        root=self.extractElement(c)
                    else:
                        manyRoots=1
            if manyRoots:
                self.log.warning("The XMI model has more than one root element. I will use the first one: ",root)
                        
        else:
            for c in node.childNodes:
                if c.nodeType!= xml.dom.Node.TEXT_NODE:
                    element=self.extractXMIContent(c)
                    if not root and element:
                        root=element

        # resolve forward references
        for t in self.secondPass.keys():
            if not self.objectById.has_key(self.secondPass[t]):
                self.log.warning("XMI contains malformed references")
            else:
                # BUG This might still be wrong??
                #print "SETATTR", t[0],t[1],self.objectById[self.secondPass[t]]
                if t[0].__dict__[t[1]] != self.objectById[self.secondPass[t]]:
                    setattr(t[0], t[1], self.objectById[self.secondPass[t]])
        return root
    
    def cannotHandle(self,node,context=''):
        if node.nodeName!='#text' and node.nodeName!='Model.Tag':
            self.log.warning("I cannot handle element "+node.nodeName)
                



### Text files

def loadTextFile(fileName):
     text=""
     try:
         fd = codecs.open(fileName,'r','latin-1','replace')
         text=fd.read()       
     finally:
         fd.close()
     return text
            
def saveTextFile(fileName,text):
    """Saves text in a file with name fileName. It may create new directories specified in fileName if necessary"""

    if os.path.dirname(fileName):
        try:
            os.makedirs(os.path.dirname(fileName))
        except:
            pass

    fd = codecs.open(fileName,'w','latin-1','replace')
    fd.write(unicode(text))
    fd.close()

__config = None

if not __config:
    __config = Configuration.Configuration()
    __config.registerParameter(
        Configuration.StringParameter("smw_server_default_port",
                                      "Port for the repository server",
                                      "8000"))
    __config.registerParameter(
        Configuration.StringParameter("smw_client_default_username",
                                      "Default anonymous username for the client",
                                      ""))
