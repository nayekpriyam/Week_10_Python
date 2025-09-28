class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            raise IndexError("dequeue from empty queue")
        return self.s2.pop()

    def peek(self):
        if self.s2:
            return self.s2[-1]
        if self.s1:
            return self.s1[0]
        return None

    def empty(self):
        return not (self.s1 or self.s2)
