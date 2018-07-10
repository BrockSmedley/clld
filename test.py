from clld import Clld

def testLoop(c):
    print "Looping through list 1.5 times..."
    x = c.head
    print x
    for i in range (c.length() + c.length()/2):
        x = c.nextItem(x)
        print x
        if (x == c.tail):
            print "end of list; looping back"
    print "Done for now.\n"

# deletes a value at a given distance from head: nn
def testDelete(c, nn):
    nn = nn%c.length()
    x = c.head
    for i in range (nn):
        x = c.nextItem(x)
    c.delete(x)
    print "Deleted item #%d..." % (nn)

def testAdd(c, n):
    c.add(n)
    print "Added an item: %d..." % (n)

def testPrev(c, n):
    print "The number before %d is %d." % (n, c.prevItem(n))

def testInit(n=None):
    c = Clld(n)
    if (n != None):
        extra = " with value %s" % (n)
    else:
        extra = ""
    print "Initialized new clld%s." % (extra)
    return c

def sanityCheck(c):
    print "Full dict: %s" % (str(c.clld))
    print "Head: %d" % (c.head)
    print "Tail: %d" % (c.tail)

def test():
    c = testInit(1)
    testAdd(c, 3)
    testAdd(c, 42)
    testLoop(c)
    testPrev(c, 1)
    testPrev(c, 42)    
    testDelete(c, 2)
    testLoop(c)
    m = [5,7,9]
    for i in m:
        testAdd(c, i)
    testLoop(c)

test()
