from collections import deque
class queue :
    def __init__(self):
        self.queue_dict = deque()
    def __len__(self):
        return len(self.queue_dict.keys())
    def push(self,item):
        self.queue_dict.appendleft(item)
    def pop(self):
        if not self.isEmpty():
            return self.queue_dict.popleft()
        else:
            print("Stack underflow")
        exit()
    def clear(self):
        self.queue_dict = deque()
    def isContain(self, item):
        return item in self.queue_dict
    def isEmpty(self):
        return len(self.queue_dict) == 0

queue_c = queue()
print(queue_c.isEmpty())
print(queue_c.push(10))
print(queue_c.isContain(10))
print(queue_c.isContain(20))
print(queue_c.isEmpty())
print(queue_c.pop())


    
    