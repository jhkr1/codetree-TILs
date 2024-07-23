class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is Empty")
        
        return self.items.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items[-1]

n = int(input())
s = Stack()
for i in range(n):
    temp = input().split()
    command = temp[0]

    if (command == 'push'):
        val = temp[1]
        s.push(val)

    elif (command == 'size'):
        print(s.size())
    
    elif (command == 'pop'):
        print(s.pop())
    
    elif (command == 'empty'):
        if(s.empty()):
            print(1)
        else:
            print(0)
    
    elif (command == 'top'):
        print(s.top())