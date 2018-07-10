### Circular-Linked List Dictionary
### Provides behavior of a circularly linked list with dictionary indexing
### Dictionary enforces unique identifiers; useful for creating simple
### databases which prioritize low storage cost
    ### Numerical values dictate no order except in
    ### their relationship to their neighbor.
    ### Thus Clld is an unordered list.
    ### example:
    ###         {123: 420, 420: 69, 82: 14, 69:82, 14:123}      
class Clld:
    # can init with array
    def __init__(self, root=None):
        self.head = None
        self.tail = None
        self.clld = {}
        
        if (type(root) == int):
            self.clld.update({root:root})
            self.head = root
            self.tail = root

        
    def add(self, val):
        # set old tail:next (currently pointing at head)
        self.clld[self.tail] = val
        # add new val to dict; point at head for circularity
        self.clld[val] = self.head
        # store new tail for later
        self.tail = val

        
    def delete(self, val):
        # transplant links from val item
        p = prevItem(val)
        n = nextItem(val)
        self.clld[p] = n

        # delete val from dict
        del self.clld[val]
        

    def nextItem(self, val):
        # simply return key's value from dict
        return self.clld[val]


    def prevItem(self, val):
        # loops all the way through the list back to the item pointing at val
        n = self.head
        while (self.clld[n] != val):
            n = self.clld[n]
        return n
