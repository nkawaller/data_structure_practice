# Uses the LinkedQueue class from 7.1.2

def breadthfirst(self):
    if not self.is_empty():
        fringe = LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)