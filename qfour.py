class Stack:
    def __init__(self):
        self.stack = [7,4]

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return ("Empty stack!")
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def show(self):
        return self.stack

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.show())
print(my_stack.pop())
print(my_stack.show())
print(my_stack.size())