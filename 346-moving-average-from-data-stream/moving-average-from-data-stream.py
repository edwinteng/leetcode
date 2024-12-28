class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.q = deque()
        self.size = size
        self.window_sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q)<self.size:
            self.q.append(val)
            self.window_sum+=val
        else:
            num = self.q.popleft()
            self.window_sum-=num
            self.window_sum+=val
            self.q.append(val)
        return self.window_sum/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)