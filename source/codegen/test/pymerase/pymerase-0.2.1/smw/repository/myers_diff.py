import copy

from diff_commands import *

def __getpath__(a, b, D,k,Vs, offset):
    result = []

    while 1:
        V = Vs.pop()
        x = V[k + offset]
        y = x - k
        if D == 0:
            #print "*** D = 0"
            assert(x == y)
            while x != 0 and y != 0:
                #print "skip %s" % a[x]
                x -= 1
                y -= 1
            break
    
        oldV = Vs[len(Vs)-1]
        # Is parent a horizontal edge?
        px = oldV[k - 1 + offset]
        py = px - (k - 1)
        px += 1

        while x > px and y > py and a[x] == b[y]:
            #print "skip %s" % a[x]
            x -= 1
            y -= 1
        
        # Horizontal movement
        if px == x and py == y:
            #print "delete %s index %d" % (a[x], x-1)
            result.append((delete_command, a[x], x-1 ))
            # We go backwards, so -1
            k -= 1
        # Vertical movement
        else:
            assert(a[x] != b[y])
            #print "insert %s index %d" % (b[y], y-1)
            result.append((insert_command, b[y], y-1))
            # We go backwards, so +1
            k += 1
            
        D -= 1

    result.reverse()

    # The indices are just plain wrong, so we fix them here.
    deletes = 0
    inserts = 0
    for i in range(len(result)):
        (command, value, index) = result[i]
        if command == delete_command:
            result[i] = (command, value, index - deletes + inserts)
            deletes += 1
        elif command == insert_command:
            inserts += 1
        else:
            assert(0)
    return result

def myers(_a, _b, emptyvalue = None):
    """Myers difference algorithm. _a is original list, _b is the new
    list. emptyvalue can be any value of the list elements, basically
    None (this is because the algorithm requires an empty row 0 and
    column 0)."""
    # Special case, no difference for empty lists
    if len(_a) == 0 and len(_b) == 0:
        return []
    
    a = copy.copy(_a)
    b = copy.copy(_b)
    a.insert(0, emptyvalue)
    b.insert(0, emptyvalue)
    alen = len(a)
    blen = len(b)
    maxlen = alen-1 + blen-1
    Vs = []
    # the value of the sentinel doesn't matter, we never hit it
    SENTINEL = -999
    # Just add maxlen to the basic algorithm to access elements
    V = [SENTINEL] * (maxlen * 2 + 1)

    # Needed for initial step
    V[maxlen+1] = 0
    
    for D in range(maxlen+1):
        for k in range(-D, D+1, 2):
            if k == -D or k != D and V[k - 1 + maxlen] < V[k + 1 + maxlen]:
                x = V[k + 1 + maxlen]
            else:
                x = V[k - 1 + maxlen] + 1
            y = x - k
            while x < alen-1 and y < blen-1 and a[x + 1] == b[y + 1]:
                x += 1
                y += 1
            V[k + maxlen] = x
            if x >= alen-1 and y >= blen-1:
                #print "Ready"
                #print "Maxlen is %d" % maxlen
                #print "D is %d" % D
                #print "k is %d" % k
                Vs.append(copy.copy(V))
                #for i in Vs:
                #    print i
                path = __getpath__(a, b, D, k, Vs, maxlen)
                return path
        Vs.append(copy.copy(V))

    # There must be a solution
    assert(0)
