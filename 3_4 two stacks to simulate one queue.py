# https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/submissions/
import collections


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # create an empty list
        self.dq_push = collections.deque()
        self.dq_pop = collections.deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.dq_push.appendleft(x)

    def peek_helper(self, should_pop):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        # deque in python: if dq --> meaning: if dq is empty, will run the following code, otherwise not
        if not self.dq_pop:
            # pull the items from one container to another
            while self.dq_push:
                temp = self.dq_push.popleft()
                self.dq_pop.appendleft(temp)

        # leftmost [0]  rightmost[-1]
        leftmost = self.dq_pop[0]
        if should_pop:
            self.dq_pop.popleft()
        return leftmost

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.peek_helper(True)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.peek_helper(False)

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if (not self.dq_pop) and (not self.dq_push):
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()