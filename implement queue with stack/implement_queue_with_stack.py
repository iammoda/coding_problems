class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.front) == 0:
            self.front.append(x)
        else:
            self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        element = self.front.pop()
        if len(self.stack) > 0:
            self.front.append(self.stack[0])
            self.stack.remove(self.stack[0])
        return element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if len(self.front) > 0 else True