# %%
class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.n = 0

    def __len__(self):
        return self.n

    def push(self,val):
        new_node = node(val)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    def pop(self):
        if self.top == None:
            return  'Empty Stack'
        self.top = self.top.next
        self.n -= 1

    def peek(self):
        if self.top  == None:
            return 'Empty Stack'
        return self.top

    def isempty(self):
        return self.top == None

    def __repr__(self) -> str:
        curr = self.top
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return str(','.join(elements))

    

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.pop()
    stack.pop()
    print(stack)
    print(stack.peek())
    print(len(stack))
        
