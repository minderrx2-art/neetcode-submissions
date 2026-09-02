class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # construct a 26 length array (for each english lower case char)
        # plus at index of the char in S
        # minus at index of the char in T
        # they should cancel out and count array should be all zeros
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for n in count:
            if n != 0:
                return False
        return True