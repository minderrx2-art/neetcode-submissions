class Solution:

    def encode(self, strs: List[str]) -> str:
        # store length:char
        encoded = "".join([str(len(s)) + ":" + s for s in strs])
        return encoded

    #5:Hello5:World
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # 3:foo
            j = s.find(":", i)
            
            # length of the string to the right (3)
            length = int(s[i:j])
            
            # append foo
            res.append(s[j + 1:j + length + 1])
            
            # left is now skipping over the rest
            i = j + length + 1
        return res