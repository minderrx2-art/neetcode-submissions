class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(s)
        st = sorted(t)
        for i in range(0,len(ss), 1):
            if ss[i] != st[i]:
                return False
        return True
