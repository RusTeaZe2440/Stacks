class Node:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.n = 0

    
    def __len__(self) -> str:
        return self.n
    
    def push(self,value):
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode
        self.n += 1

    def pop(self):
        if self.top == None:
            return 'Empty Stack'
        data = self.top.val
        self.top = self.top.next
        self.n -= 1
        print(data)
    
    def peek(self):
        if self.top == None:
            return 'Empty Stack'
        else:
            return self.top.val
        
    def is_empty(self):
        return self.top == None
    
    def __str__(self) -> str:
        if self.top == None:
            return 'Empty Stack'
        curr = self.top
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        
        return str('|'.join(elements))


if __name__ == "__main__":
    s = Stack()
    s = Stack()
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    print(s)
    print('Poped Item')
    s.pop()
    s.pop()
    print(s)