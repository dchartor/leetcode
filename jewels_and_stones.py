def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        am = 0
        for i in J:
            for j in S:
                if i == j:
                    am += 1
                    S = S.replace(j, '')

        return am

print(numJewelsInStones('bcd', 'cba'))
