def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x[:len(x)//2 + 1] == x[len(x) // 2::-1]

print(isPalindrome(121))
