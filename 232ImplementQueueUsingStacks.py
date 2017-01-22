class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        self.aux=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack:
            self.aux.append(self.stack.pop())
        self.stack=[x]
        while self.aux:
            self.stack.append(self.aux.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return(self.stack.pop())

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return(self.stack[-1])

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return(self.stack==[])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
