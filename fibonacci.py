def fib(N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a
fib(4)
