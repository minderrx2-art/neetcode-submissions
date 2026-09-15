class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        match len(s):
            case l if l == 0:
                return 0
            case l if l == 1:
                return 1
        
        i,j = 0,0
        ans = 0
        
        while j < len(s):
            # When we find an existing character we shrink
            # The sliding window from the left
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            ans = max(ans, len(chars))
            j += 1
        return ans