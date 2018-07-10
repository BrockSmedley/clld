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
    ### Constructor. Optional init with root value.
    def __init__(self, root=None):
        self.refresh(root)

    ### clears list, optionally sets new root
    def refresh(self, newVal=None):
        self.head = None
        self.tail = None
        self.clld = {}
        if (type(newVal) == int):
            self.head = newVal
            self.tail = newVal
            self.clld.update({newVal:newVal})

    ### add new value to list
    def add(self, val):
        if (self.tail == None or self.head == None):
            # must be the first item; late initialization OK (:
            self.refresh(val)
        else:
            # set old tail:next (currently pointing at head)
            self.clld[self.tail] = val
            # add new val to dict; point at head for circularity
            self.clld[val] = self.head
            # store new tail for later
            self.tail = val

    ### delete a specific value from the list
    def delete(self, val):
        # transplant links from val item
        p = self.prevItem(val)
        n = self.nextItem(val)
        if (val == self.tail): # if we delete tail, update it
            self.tail = p
        elif (val == self.head): # if we delete head, update it
            self.head = n
        self.clld[p] = n

        # delete val from dict
        del self.clld[val]

        
    ### returns item "pointed to" by val
    def nextItem(self, val):
        # simply return key's value from dict
        return self.clld[val]

    ### returns item "pointing to" val
    def prevItem(self, val):
        # loops all the way through the list back to the item pointing at val
        n = self.head
        while (self.clld[n] != val):
            n = self.clld[n]
        return n

    ### returns length of list
    def length(self):
        return len(self.clld.keys())
