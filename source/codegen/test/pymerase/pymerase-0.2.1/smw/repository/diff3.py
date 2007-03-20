#
# Routines for diff3 / patch3
#
# This is needed when we update (==apply a patch) a (part of a)
# model when we have already changed it a bit.
#
#  |
#  |  original model
#  |        /   \
#  |       /     \
#  | MD_A /       \ MD_B
#  |     /         \
#  |    /           \
#  | new revision    changed revision
#  |           \       |
#  |   (N/A)    \      | new MD_A
#  |             \     |
#  |              result
# \|/
#
#  time
#

#
# WHAT WE DO
#
# Get the ModelDifference A between original_model and new_revision
# Get the ModelDifference B between original_model and changed_revision
#
# As we already have the changed_revision as a model (it's after
# all what the user sees in the monitor, or the repository server
# has already checked out), we will MODIFY the ModelDifference A so
# it will apply cleanly to changed_revision.
#
# Various conflicts will be reported, and the user will "somehow" be able
# to resolve this
#
#

#
# HOW WE DO IT
#
# By assumption, any newly created element can't be in both
# ModelDifferences due to XMI id uniqueness. So newly created elements
# are left intact.
#
# Destroyed elements (in MD_A or MD_B) are valid if the other MD
# doesn't do any changes to the element in question. Otherwise, conflict.
#
# Some simple consolidations:
# * If both MDs delete the same element from an association, we modify MD_A
#   to not delete (since MD_B has already deleted it) NOT AVAILABLE
# * If both MDs want to delete the same element from the model, we modify
#   MD_A to not delete (since MD_B has already deleted it)
# * If both MDs modify the same attribute to the same value
#
# Possible conflict situations:
# * MD_A modifies an element that MD_B wants to delete, or vice versa
# * MD_A adds an element to an ordered association at the same place as MD_B
# * MD_A modifies the same attribute as MD_B.
#
#

import string
from smw.repository.diff_commands import *
from smw.repository.diff import *
from smw.metamodel.Reflection import getMetamodelByName
from smw.metamodel.MetaMM import MMClass


def __get_hash_of_touched_uuids__(md):
    result = {}
    for (uuid, editscript) in md.element_differences:
        if not result.has_key(uuid):
            result[uuid] = []
        result[uuid].append( (uuid,editscript) )

    return result



def __set_delta__(imp, uuid, key, ec):
    command = ec.command
    
    if not imp.has_key((uuid, key)):
        imp[(uuid, key)] = []

    ourlist = imp[(uuid, key)]

    if isinstance(ec, ElementSingleAssociationChange):
        assert(command == change_one_association)
        assert(len(ourlist) == 0)
        ourlist.append ( -1 ) # Mark it accessed by the MD
        return
    if ec.thisEndUnordered():
        ourlist.append ( -2 ) # Mark it accessed by the MD
        return
    
    assert(command != change_one_association)
    
    index = ec.index
    print "set_delta", imp, uuid, key, command, index

    # Default last item
    take = len(ourlist)-1

    for i in range(len(ourlist)):
        (high_index, high_add, high_del) = ourlist[i]
        if high_index < index:
            continue
        # Take the previous
        i -= 1
        if i == -1:
            assert(index == 0) # ?
            if command == insert_command:
                ourlist.insert(0, [0, 1, 0])
            elif command == delete_command:
                ourlist.insert(0, [0, 0, 1])
            else:
                assert(0)
            return
        else:
            take = i
            break

    print take
    if len(ourlist) > 0:
        (high_index, high_add, high_del) = ourlist[take]
        high_delta = high_add + high_del
        if high_delta < 0:
            high_delta = 0
        if high_index + high_delta >= index:
            # Just modify delta
            if command == insert_command:
                ourlist[take][1] += 1
            elif command == delete_command:
                ourlist[take][2] += 1
            else:
                assert(0)
            return

    if command == insert_command:
        ourlist.insert(take, [index, 1, 0])
    elif command == delete_command:
        ourlist.insert(take, [index, 0, 1])
    elif command == change_one_association:
        # Already taken care of in the beginning
        assert(0)
    else:
        assert(0)

    return

def __find_in_other_md__(modeldifference, uuid, key, elemchange):
    """Finds an elemchange in modeldifference, with given uuid and key,
    that is similar to the given elemchange. Returns None
    if not found."""
    b_elemdiff = None
    for (b_uuid, b_ed) in modeldifference.element_differences:
        if b_uuid == uuid:
            b_elemdiff = b_ed
            break
    if b_elemdiff == None:
        return None

    if not b_elemdiff.element_editscripts.has_key(key):
        return None

    b_elemchanges = b_elemdiff.element_editscripts[key]

    b_ec = None
    for i in b_elemchanges:
        if elemchange.isSimilarTo(i):
            b_ec = i
            break

    return b_ec

def __find_elemdiff__(MD, uuid, key):
    """Finds the elemdiff of uuid/key in MD."""
    elemdiff = None
    for (o_uuid, o_elemdiff) in MD.element_differences:
        if o_uuid == uuid:
            elemdiff = o_elemdiff
            break
    if not elemdiff:
        return None
    if not elemdiff.element_editscripts.has_key(key):
        return None
    return elemdiff

def __get_corresponding_ec__(MD, module, uuid, key, elemchange, elemdiff, which_one = 0):
    """Returns the corresponding elemchange(s).
    For ElementChange, it returns the other instance. Must be found.
    Note, we return a list of them, because due to indices there might be multiple
    candidates.
    For ElementSingleAssociationChange, it returns the "from" (which_one == -1)
    or "to" (which_one == 1). Must be found.
    """
    element_type = getattr(module, elemdiff.element_type)
    other_key = element_type.__mm__[key][3]

    if isinstance(elemchange, ElementChange):
        other_uuid = elemchange.value
        command = elemchange.command
 
    elif isinstance(elemchange, ElementSingleAssociationChange):
        if which_one == -1:
            other_uuid = elemchange.frm
            command = delete_command
            
        elif which_one == 1:
            other_uuid = elemchange.to
            command = insert_command
        else:
            assert(0)
    else:
        assert(0)

    ed = __find_elemdiff__(MD, other_uuid, other_key)
    ecs = ed.element_editscripts[other_key]
        
    candidates = []
    for i in ecs:

        if isinstance(i, ElementChange):
            # NOTE, we don't care about the index!
            if i.command == command and i.value == uuid:
                candidates.append(i)

        elif isinstance(i, ElementSingleAssociationChange):
            assert(i.command == change_one_association)
            if command == delete_command:
                s = i.frm
            elif command == insert_command:
                s = i.to
            if s == uuid:
                candidates.append(i)
            # Since this is the one and only elemchange, the for loop
            # will exit after this. No break needed.

    assert(len(candidates) > 0)
    return (ed, other_uuid, other_key, candidates)

def __cycle_through_single_association__(MD, module, uuid, key, elemchange, elemdiff, which_direction):
    # list of (uuid, key, ec)
    get_these_similars = []

    cyclic = 0
    
    ec = elemchange
    ec_uuid = uuid
    ec_key = key
    ec_elemdiff = elemdiff
    while ec:
        if ec in get_these_similars:
            assert(ec == elemchange)
            # cyclic, we should skip .to direction, it should be unnecessary
            cyclic = 1
            break
        
        get_these_similars.append((ec_uuid, ec_key, ec))
        if not ec.frm:
            break
        (next_elemdiff, next_uuid, next_key, next_corr_ecs) = __get_corresponding_ec__(MD_A, module, ec_uuid, ec_key, ec, ec_elemdiff, which_direction)
        # must find exactly one.
        assert(len(next_corr_ecs) == 1)
        ec_uuid = next_uuid
        ec_key = next_key
        ec_elemdiff = next_elemdiff
        ec = next_corr_ecs[0]

    return get_these_similars, cyclic

def __try_to_drop__(MD_A, MD_B, imp, module, uuid, key, elemchange, elemdiff):
    """This routine tries to find similar changes in MD_A and MD_B and DROPS
    them from MD_A if possible.

    Note that we have many combinations,
    * ins/ins
    * del/del
    * ins-change-del
    * del-change-ins
    * change-change-change... (argh)
    """
    
    element_type = getattr(module, elemdiff.element_type)

    drop_these = []
    
    #
    # 1. first find exactly the similar elemchange in MD_B as we have now.
    #
    b_ec = __find_in_other_md__(MD_B, uuid, key, elemchange)
    if b_ec == None:
        return 0
    print "FOUND", b_ec

    #
    # 2. get the corresponding (dual) elemchanges in MD_A
    # For ElementChange, the target can be an ElementChange or a
    # ElementSingleAssociationChange.
    #
    # For ElementSingleAssociationChange, the target can be
    # either an ElementChange or a ElementSingleAssociationChange.
    #

    if isinstance(elemchange, ElementChange):

        drop_these.append(elemchange)
    
        print MD_A
        (other_elemdiff, other_uuid, other_key, corr_ecs) = __get_corresponding_ec__(MD_A, module, uuid, key, elemchange, elemdiff)

        # corr_ecs is a list... test them all, not just the first one
        b_ec_other = None
        for corr_ec in corr_ecs:
            b_ec_other = __find_in_other_md__(MD_B, other_uuid, other_key, corr_ec)
            if b_ec_other:
                # BUG we should try the isinstance thing below
                # if it works, sweet, drop it all, otherwise
                # continue iterating here...
                break

        if not b_ec_other:
            return 0

        print "FOUND OTHER", b_ec_other

        #
        #
        # Right, the ins/ins or del/del case is done
        #
        #
        
        # Cool, we can drop these changes!
        drop_these.append(corr_ec)

        #
        #
        # ins-change-del / del-change-ins
        #
        #
        if isinstance(corr_ec, ElementSingleAssociationChange):
            which = 0
            quit = 0
            
            # Search for opposite
            if elemchange.command == insert_command:
                which = -1
                # ins-change
                if corr_ec.frm == None:
                    quit = 1
            elif elemchange.command == delete_command:
                which = 1
                # del-change
                if corr_ec.to == None:
                    quit = 1
            else:
                assert(0)
            print "XXXX", elemchange, which

            # BUG BUG BUG third_corr_ecs is a list... test them all, not just the first one

            if not quit:
                (third_elemdiff, third_uuid, third_key, third_corr_ecs) = __get_corresponding_ec__(MD_A, module, other_uuid, other_key, corr_ec, other_elemdiff, which)
                third_corr_ec = third_corr_ecs[0]
                assert(third_key == key)
                assert(third_corr_ec != elemchange)
            
                b_ec_third = __find_in_other_md__(MD_B, third_uuid, third_key, third_corr_ec)
                
                if not b_ec_third:
                    # uh oh, something fishy going on
                    # We have a ins-change-del or del-change-ins set of changes,
                    # but the last one wasn't found
                    # I think this is post-thesis material...
                    return 0
                print "FOUND THIRD", b_ec_third
                drop_these.append(third_corr_ec)

    elif isinstance(elemchange, ElementSingleAssociationChange):
        #
        #
        # We really only have to take care of the change-change-change thing,
        # not ins-change-del, SINCE IT WILL BE CALLED from somewhere else,
        # i.e., from the ins or del part
        # NOTE: This is perhaps a bit cheating...
        #
        #
        if element_type.__mm__[key][4] != 1:
            return 0

        #
        # OK, so now we collect the list of elemchanges, and always
        # check that there is a corresponding one. When we've gone through it
        # all => drop them if similars are all found in MD_B.
        #

        get_these_similars = []

        #
        # We have to walk both the .frm and .to paths, since it might not
        # be circular.
        #

        # .frm direction
        gs, cyclic =  __cycle_through_single_association__(MD_A, module, uuid, key, elemchange, elemdiff, -1)
        get_these_similars.extend(gs)
        if not cyclic:
            # .to direction
            gs, cyclic =  __cycle_through_single_association__(MD_A, module, uuid, key, elemchange, elemdiff, 1)
            assert(cyclic == 0)
            get_these_similars.extend(gs)

        for (ec_uuid, ec_key, ec) in get_these_similars:
            MD_B_elemchange = __find_in_other_md__(MD_B, ec_uuid, ec_key, ec)
            if not MD_B_elemchange:
                # not everything matched, so we must go away. too bad.
                return 0

        # we found a list of ec:s that both MD:s have, drop them all in MD_A
        for (ec_uuid, ec_key, ec) in get_these_similars:
            drop_these.append(ec)

    else:
        assert(0)
    #
    # 3. and find similar in MD_B => drop them all in MD_A!
    #
    if len(drop_these) == 0:
        return 0

    #
    # Uh. slow drop
    #
    for (d_uuid, d_elemdiff) in MD_A.element_differences:
        for d_key in d_elemdiff.element_editscripts.keys():
            ecs = d_elemdiff.element_editscripts[d_key]
            for i in copy.copy(drop_these): # walk safely
                if i in ecs:
                    ecs.remove(i)
                    drop_these.remove(i)

    return 1

        
def __fix_delta__(MD_A, MD_B, imp, module, uuid, key, elemchange, elemdiff):
    """imp contains all ordered deltas from B. uuid is "this" uuid, and key
    is our key."""

    print "fix_delta", imp
    #print "fix_delta", uuid, key, otherkey, elemchange, this_end, other_end
    if not imp.has_key((uuid, key)):
        print "Nothing to do for ", uuid, key
        return []

    if __try_to_drop__(MD_A, MD_B, imp, module, uuid, key, elemchange, elemdiff):
        return []

    element_type = getattr(module, elemdiff.element_type)

    mc = None
    if element_type.__mm__[key][2] == 1:
        assert(imp[(uuid, key)] == [ -1 ] )
        other_ec = __find_elemdiff__(MD_B, uuid, key).element_editscripts[key][0]
        mc = MCChangeSingleMultiplicity(elemdiff, elemchange, { "B": other_ec.to, "A": elemchange.to })
    else:
        if MetaMM.isOrdered(element_type.__mm__, key):
            mc = __fix_delta_one__(imp[(uuid, key)], elemdiff, elemchange)

    return [mc]

def __fix_delta_one__(ourlist, elemdiff, elemchange):

    command = elemchange.command
    index = elemchange.index
    print "fix_delta_one", ourlist
    print "fix_delta_one", elemchange, command, index
    maxlen = len(ourlist)

    mc = None

    for i in range(maxlen+1):
        if i != maxlen:
            (high_index, high_add, high_del) = ourlist[i]

            print high_index, high_add, high_del

            if high_index <= index:
                index += high_add - high_del
                continue

        # i could be 0
        if i == 0:
            # Don't do anything, this is clean
            return None

        # Take the previous
        i -= 1
        (high_index, high_add, high_del) = ourlist[i]
        high_delta = high_add - high_del
        # Take back previous delta
        index -= high_delta

        assert(high_index <= index)

        print "* index ", index
        print "* high", high_index, high_add, high_del
        
        if command == delete_command:

            if high_index + high_del > index:
                # TROUBLE
                # Deleting something already deleted
                print "TROUBLE: Deleting something already deleted?", command, index
                # The hash is probably not good enough
                mc = MCAlreadyDeleted ( elemdiff, elemchange, {"index": index } )
                # Set index?
                
            else:
                # ok, deletion outside
                index += high_delta

        elif command == insert_command:
            # outside
            if high_index + high_del < index:
                index += high_delta
                assert(high_index <= index)
            # No additions, just insert at high_index
            elif high_add == 0:
                #
                # BUG: This has the problem that a later
                # addition at a higher index can "fall back"
                # at high_index as well, meaning it will be inserted
                # _before_ this current stuff, instead of after it
                #
                index = high_index
            # The interesting case
            # 1) inside, 2) Additions, 3) perhaps deletions
            else:
                # TROUBLE
                # On which side do we do the insert?
                print "TROUBLE: On which side do we do the insert?", command, index
                mc = MCWhichSide ( elemdiff, elemchange, {"index": high_index, "length": high_add } )
                # Set index, default is after these people...
                index = high_index + high_add
        else:
            assert(0)

        break


    if index != -1:
        elemchange.index = index
        
    return mc


def diff3(basemodel, MD_A, MD_B, module = None):
    """Modifies MD_A according to MD_B. Returns the new MD_A and
    a list of conflicts. You can give the metamodel python module
    as a parameter for faster execution. basemodel is not used
    at the moment."""

    # Assume metamodel for MD_A is same
    assert(MD_A.metamodel_name == MD_B.metamodel_name)

    if not module:
        module = getMetamodelByName(MD_B.metamodel_name)

    uuids_A = __get_hash_of_touched_uuids__(MD_A)
    uuids_B = __get_hash_of_touched_uuids__(MD_B)

    print "uuids_A"
    for o in uuids_A.keys():
        print o, uuids_A[o]

    print "uuids_B"
    for o in uuids_B.keys():
        print o, uuids_B[o]
    print
    print
    #
    # Important dict.
    # It contains (uuid, key) => [(this-or-above-number,
    # delta-positive, delta-negative)...]
    # Which means that when we want to check an insertion/deletion
    # We grab its index, and search for the highest this-or-above-number
    # that is =< index.
    #
    important_delta = {}

    # Map of (uuid, key) => (cmd, frm, to)
    change_attributes = {}

    for (uuid, elemdiff) in MD_B.element_differences:
        # Not supported
        assert(not elemdiff.change_xmiid)
        # Not supported
        assert(not elemdiff.change_type)

        print "Check ", uuid #, uuids_B[uuid]

        # OK, so this contains editscripts which change
        # the behaviour of MD_A

        element_type = getattr(module, elemdiff.element_type)

        for key in elemdiff.element_editscripts.keys():
            # Skip attributes
            if element_type.__mm__[key][0] == MMClass.kind__Attribute:
                continue
            print "key", key
            val = elemdiff.element_editscripts[key]

            for i in val:
                __set_delta__(important_delta, uuid, key, i)

        # Attributes
        for key in elemdiff.element_editscripts.keys():
            # Skip all but attributes
            if not element_type.__mm__[key][0] == MMClass.kind__Attribute:
                continue

            ec = elemdiff.element_editscripts[key][0]
            cmd, frm, to = ec.command, ec.frm, ec.to

            assert(cmd == change_attribute_command)
            change_attributes[(uuid, key)] = (cmd, frm, to)

    #
    #
    # Good, now we have populated important_delta correctly
    # Now fix MD_A indices.
    #
    #

    print
    print "********************"
    print "* Important deltas *"
    print "********************"
    print important_delta
    print

    # This jump just to de-pollute the variable namespace...
    __next_step__(MD_A, MD_B, important_delta, change_attributes, module)
    MD_A.is_diff3 = 1

    MD_A.cleanup(MD_B)

    MD_A.updateMergeConflicts()

    return MD_A.mergeconflicts

def __next_step__(MD_A, MD_B, important_delta, change_attributes, module):
    for (uuid, elemdiff) in MD_A.element_differences:
        # Not supported
        assert(not elemdiff.change_xmiid)
        # Not supported
        assert(not elemdiff.change_type)

        element_type = getattr(module, elemdiff.element_type)

        for key in elemdiff.element_editscripts.keys():
            if element_type.__mm__[key][0] == MMClass.kind__Attribute:
                continue
            print "key", key
            
            elem_changes = elemdiff.element_editscripts[key]
            # create a copy of the list, since we might drop stuff in __try_to_drop__.
            for elemchange in copy.copy(elem_changes):
                # If it got destroyed by some _really_ evil
                # metamodel. This should most likely never happen.
                if elemchange not in elem_changes:
                    # I don't think all of smw can handle stuff this weird.
                    print "**********************************************************************"
                    print "* diff3.py:Odd metamodel                                             *"
                    print "**********************************************************************"
                    continue
                
                print "EC"
                print elemchange

                new_mcs = __fix_delta__(MD_A, MD_B, important_delta, module, uuid, key, elemchange, elemdiff)

                # NO, we do this later... 
                # # Add merge conflicts
                # for mc in new_mcs:
                #     if mc:
                #         mcs.append(mc)
        # Attributes
        for key in elemdiff.element_editscripts.keys():
            if not element_type.__mm__[key][0] == MMClass.kind__Attribute:
                continue
            ec = elemdiff.element_editscripts[key][0]
            cmd, frm, to = ec.command, ec.frm, ec.to
            assert(cmd == change_attribute_command)
            if change_attributes.has_key((uuid, key)):
                t = change_attributes[(uuid, key)]
                assert(t[0] == change_attribute_command)
                # NOTE
                #
                # If first MD changes (A, NULL) and second
                # changes (A, B), we can change the second
                # to (NULL, B) and things work.
                # Well, most of the time anyway
                #
                if 0: # NOT ACTIVATED....
                    if (not t[2]):
                        if not frm: # Already changed
                            continue
                        assert(t[1] == frm)
                        elemdiff.element_editscripts[key] = [ ElementAttributeChange(change_attribute_command, t[2], to) ]
                        continue

                
                assert(t[1] == frm) # Otherwise the differences are bad
                if t[2] == to:
                    # woot, we are changing to the same thing
                    # DROP this change!
                    # This del works (should work) since we are
                    # iterating through the keys() sequence in the loop
                    del elemdiff.element_editscripts[key]
                    continue

                # Otherwise, conflict
                MCAttribute( elemdiff, ec, {"B": t[2], "A": to})

    return []

            


class MergeConflict:
    """A merge conflict between two model differences."""

    def __init__(self, elemdiff, elemchange, hash_of_info):
        self.elemdiff = elemdiff
        self.elemchange = elemchange
        self.hash_of_info = hash_of_info

        elemchange.attachMergeConflict(self)

    def __str__(self):
        t = "MergeConflict:\n" + \
            "Type:  "
        if isinstance(self, MCAlreadyDeleted):
            t +="Index already deleted by other ModelDifference\n"
        elif isinstance(self, MCWhichSide):
            t += "Index can be on either side of the other difference\n"
        elif isinstance(self, MCAttribute):
            t += "Attribute changed in both ModelDifferences\n"
        elif isinstance(self, MCChangeSingleMultiplicity):
            t += "Multiplicity == 1, and both MD:s change it\n"
        else:
            assert(0)
            
        t +="Elemchange Id: " + str(self.elemchange) + "\n"
        t +="Extra:\n"
        for i in self.hash_of_info.keys():
            t +="       %s: %s\n" % (str(i), str(self.hash_of_info[i]))
        return t

    def drop(self):
        """Drop this MergeConflict."""
        self.elemchange.removeMergeConflict(self)
        self.elemdiff = None
        self.elemchange = None

    def dropElemChange(self):
        """Drops the corresponding elemchange, and this MergeConflict."""
        self.elemdiff.remove(self.elemchange)
        self.elemchange.removeMergeConflict(self)

class MCAlreadyDeleted(MergeConflict):
    def __init__(self, elemdiff, elemchange, hash_of_info):
        MergeConflict.__init__(self, elemdiff, elemchange, hash_of_info)
    # basically, these can only be dropElemchanged?
    

class MCChangeSingleMultiplicity(MergeConflict):
    def __init__(self, elemdiff, elemchange, hash_of_info):
        MergeConflict.__init__(self, elemdiff, elemchange, hash_of_info)

    def getAlternatives(self):
        return self.hash_of_info["A"], self.hash_of_info["B"]

    def resolveNewSingleMultiplicity(self, new_attrib_name):
        # Quite identical to MCAttribute.resolveNewAttribute
        ec = self.elemchange
        cmd, frm, to = ec.command, ec.frm, ec.to
        
        assert(cmd == change_one_association)

        if new_attrib_name == self.hash_of_info["A"]:
            # B name already applied, so the change is from B to A
            self.elemdiff.element_editscripts[key] = [ ElementAttributeChange(cmd, self.hash_of_info["B"], new_attrib_name) ]
            # No need to drop, since the whole ElementAttributeChange
            # was dropped => implicitely dropped
                                                     
        elif new_attrib_name == self.hash_of_info["B"]:
            # B name already applied, so we have no change
            self.dropElemChange()
            
        else:
            assert(0)

class MCWhichSide(MergeConflict):
    def __init__(self, elemdiff, elemchange, hash_of_info):
        MergeConflict.__init__(self, elemdiff, elemchange, hash_of_info)

    def getIndexAndLength(self):
        return self.hash_of_info["index"], self.hash_of_info["length"]

    def resolveSide(self, new_index):
        # Resolve to either left or right-hand side
        assert(new_index == self.hash_of_info["index"] or new_index == self.hash_of_info["index"] + self.hash_of_info["length"])

        self.elemchange.index = new_index

        # Remove the MC now that it has been resolved
        self.drop()

class MCAttribute (MergeConflict):
    def __init__(self, elemdiff, elemchange, hash_of_info):
        MergeConflict.__init__(self, elemdiff, elemchange, hash_of_info)

    def getAlternatives(self):
        return self.hash_of_info["A"], self.hash_of_info["B"]
        
    def resolveNewAttribute(self, new_attrib_name):
        ec = self.elemchange
        cmd, frm, to = ec.command, ec.frm, ec.to
        
        assert(cmd == change_attribute_command)

        if new_attrib_name == self.hash_of_info["A"]:
            # B name already applied, so the change is from B to A
            ec.frm = self.hash_of_info["B"]
            ec.to  = new_attrib_name
            # No need to drop, since the whole ElementAttributeChange
            # was dropped => implicitely dropped
            self.drop()
            
        elif new_attrib_name == self.hash_of_info["B"]:
            # B name already applied, so we have no change
            self.dropElemChange()
            
        else:
            assert(0)
