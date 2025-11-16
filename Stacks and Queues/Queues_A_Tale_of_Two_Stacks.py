class MyQueue(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def put(self, value):
        self.stack_in.append(value)
    
    def _shift(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def peek(self):
        self._shift()
        return self.stack_out[-1]
        
    def pop(self):
        self._shift()
        return self.stack_out.pop()

