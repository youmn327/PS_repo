class stack :
    def __init__(self):
        self.top = []
    def __len__(self):
        return len(self.top)
    def __str__(self):
        return str(self.top[::1])
    def push(self,item):
        self.top.append(item)
        return "success"
    def pop(self):
        if not self.isEmpty():
            return self.top.pop()
        else:
            print("Stack underflow")
        exit()
    def clear(self):
        self.top = []
    def isContain(self, item):
        return item in self.top
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()
    def isEmpty(self):
        return len(self.top) == 0
    
stack_c = stack()
print(stack_c.isEmpty())
print(stack_c.push(10))
print(stack_c.isContain(10))
print(stack_c.isContain(20))
print(stack_c.isEmpty())
print(stack_c.peek())
print(stack_c.pop())


    
    