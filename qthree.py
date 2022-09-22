class Queue:
    def __init__(self):
        self.queue = [1, 2]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        return self.queue

my_queue = Queue()
my_queue.isEmpty()
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
print("Before perfroming the dequeue, size: ")
print(my_queue.size())
my_queue.dequeue()
print("After doing the dequeue, size: ")
print(my_queue.size())
print(my_queue.show())
