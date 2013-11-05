
row1 = ['1','2','3','4','5','6','7','8','9','0']

class Node(object):
    data = None
    next = None
    previous = None
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
        self.previous = None
    
    def addNext(self, node):
        self.next = node
        node.previous = self.next
        
    def hasNext(self):
        if self.next is not None:
            return True
        
        return False

    def hasPrevious(self):
        if self.previous is not None:
            return True
        
        return False

class LinkedList(object):
    nodes = []
    first = None
    last = None
    
    def __init__(self, root):
        self.first = root
        self.last = root
    
    # Find the last node.
    def findLastNode(self, node):
        if not node.hasNext():
            self.last = node
        else:
            findLastNode(node.next)
    
    # Node is added to the end of the list.
    def addNode(self, node):
        # Add the node 
        self.last.addNext(node)
        
        # Set the last node correctly.
        self.last = node
    
    def output_list(self):
        node = self.first
        output = ""
        while node.hasNext():
            output = "%s%s -> " % (output, node.data)
            
            node = node.next
        
        output = "%s%s" % (output, node.data)
        
        print output

keyboard = []

def buildKeyboard():
    first_row = ['1','2','3','4','5','6','7','8','9','0']
    second_row = ['q','w','e','r','t','y','u','i','o','p']
    third_row = ['a','s','d','f','g','h','j','k','l',';']
    fourth_row = ['z','x','c','v','b','n','m',',','.','/']
    
    global keyboard 
    keyboard = [first_row,
                second_row,
                third_row,
                fourth_row]
    
    '''
    keyboard_ll = []
    
    for row in keyboard:
        ll = None
        for element in row:
            node = Node(element)
        
            if ll is None:
                ll = LinkedList(node)
            else:
                ll.addNode(node)
        
        keyboard_ll.append(ll)
    
    return keyboard_ll
    '''

def H():
    global keyboard
    
    for row in keyboard:
        row.reverse()

def V():
    global keyboard
    
    index = 0
    swapIndex = len(keyboard) - 1
    
    while index < swapIndex:
        temp_row = keyboard[index]
        keyboard[index] = keyboard[swapIndex]
        keyboard[swapIndex] = temp_row
        
        index += 1
        swapIndex -= 1

def shift(amount):
    global keyboard

    # We're going to flatten the list.
    flat_list = []
    for row in keyboard:
        for item in row:
            flat_list.append(item)
    
    if amount > 0:
        # Find the index where to splice the list.
        index = len(flat_list)-amount
    else:
        # Find the index again, though this time with a negative number.
        # This is also simply saying that the first 'amount' of items is shifting
        # to the end of the list.
        index = abs(amount)
    
    # Now create the new list. You take the sublist of the index to the end, move
    # that to the front, then take the start to the index and move it to the end.    
    new_list = flat_list[index:] + flat_list[:index]
    
    # Now we need to move it back to the keyboard representation.
    
    print new_list
        
def print_keyboard():
    for row in keyboard:
        print row

'''
    Main Method for testing.
'''
if __name__ == '__main__':
    buildKeyboard()
    
    #H()
    #V()
    
    shift(-5)
    
    #print keyboard
    