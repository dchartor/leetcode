def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
    return (sum(l) - sum(set(l))) / (len(l) - len(set(l)))
