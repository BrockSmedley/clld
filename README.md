# clld
Circular singly-linked list implemented in a Python2 dictionary.

Dictionaries enforce unique IDs and inherently have a "pointing" capability within their native mapping scheme. For a data store which requires unique entries and iterative searchability, this is a nice solution which keeps memory costs low. 

Deletes are relatively CPU-intensive; Θ(N); but accesses and adds are O(1).
