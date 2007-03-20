import string

from smw.metamodel.OCLforPython import MMSet
from smw.metamodel.MetaMM import MMClass


class SRAttribute:
    def __init__(self,name,aType,aTypeName,multiplicity):
        self.name=name
        self.aType=aType
        self.aTypeName=aTypeName
        self.multiplicity=multiplicity
        
class SRAssociationEnd:
    def __init__(self,name,otherType,otherTypeName,
                 aggregation,multiplicity,otherAssociationEnd,ordered):
        self.name=name
        self.otherType=otherType
        self.otherTypeName=otherTypeName
        self.aggregation=aggregation
        self.multiplicity=multiplicity
        self.otherAssociationEnd=otherAssociationEnd
        self.ordered=ordered

class SimpleReflector:
    def __init__(self,subject):
        self.name=subject.__name__
        self.generalization=MMSet(subject.__bases__)
        try:
            self.specialization=MMSet(subject.__subclasses__)
        except:
            self.specitialization=MMSet()
        self.aType=subject
        self.feature=MMSet()
        for k in subject.__mm__.keys():
            if subject.__mm__[k][0]==MMClass.kind__Attribute:
                self.feature.insert(SRAttribute(k,
                                  subject.__mm__[k][1],
                                  subject.__mm__[k][1].__name__,
                                  subject.__mm__[k][2]))
        self.association=MMSet()
        for k in subject.__mm__.keys():
            if subject.__mm__[k][0]!=MMClass.kind__Attribute:
                self.association.insert(SRAssociationEnd(k,
                                  subject.__mm__[k][1],
                                  subject.__mm__[k][1].__name__,
                                  subject.__mm__[k][0],
                                  subject.__mm__[k][2],
                                  subject.__mm__[k][3],
                                  subject.__mm__[k][4],
                                  ))

def getMetamodelByName(name):
    """Returns a Python metamodel module for the modeling language
    name.  name is a string and it can contain spaces and dots, for
    example 'UML 1.3' or 'UML1.3'. It can also be a string containing
    a fully quallified module, for example 'smw.metamodel.UML13' """

    if string.find(name,"metamodel")==-1 and \
           string.find(name,"profiles")==-1:
        if '.' in name or ' ' in name:
            # 'UML 1.1' becomes 'UML11'
            name=string.replace(name,'.','')
            name=string.replace(name,' ','')
        
        modulename="smw.metamodel."+name
    else:
        modulename=name
    module=__import__(modulename,globals(),locals(),
                      [string.split(modulename,'.')[-1]]
                      )            
    return module
