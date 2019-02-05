def uniqueMorseRepresentations(words):
        """
        :type words: List[str]
        :rtype: int
        """

        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len(set(''.join(alphabet[ord(c) - ord('a')] for c in word) for word in words))
