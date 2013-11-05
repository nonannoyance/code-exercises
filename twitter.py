"""
powerset of integers: [1,2,3]
[
[],
[1],
[2],
[3],
[1,2],
[1,3],
[2,3],
]

def powerset(seq):
    # Returns all the subsets of this set. This is a generator.
    
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
"""

class Node(object):
    data = None
    descendant = None

    def __init__(self, data=None):
        self.data = data

    def setDescendant(self, node):
        self.descendant = node
        
        
def isPalindrome(string):
    index = 0
    length = len(string)
    pivot = length/2
    
    # Want to check the back end of the string from the front end.
    # We know the 'middle' character is the pivot.
    while index < pivot:
        if string[index] != string[(length-1)-index]:
            return False
        
        index += 1
    
    return True