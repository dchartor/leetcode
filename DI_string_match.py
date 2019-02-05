def diStringMatch(S):
        """
        :type S: str
        :rtype: List[int]
        """

        x, y = 0, len(S)

        newl = []

        for i in range(len(S)):
            if S[i] == 'I':
                newl.append(x)
                x += 1
            elif S[i] == 'D':
                newl.append(y)
                y -= 1
        return newl + [x]

diStringMatch('DIDI')

#l = [0, 1, 2, 3, 4]

#print(l)
