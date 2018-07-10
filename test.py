from clld import Clld

def test():
    c = Clld(1)
    c.add(3)
    c.add(42)
    x = c.head
    print x
    for i in range (5):
        x = c.nextItem(x)
        print x
        if (x == c.tail):
            print "end of list; looping back"

test()
