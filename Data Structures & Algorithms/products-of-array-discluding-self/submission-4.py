class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.prefixProd(nums)
        suffix = self.suffixProd(nums)

        ans = []
        for i,n in enumerate(nums):
            if i - 1 < 0:
                ans.append(suffix[i + 1])
            elif i + 1 > len(nums) - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i-1] * suffix[i+1])
        return ans
    
    def prefixProd(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 1
        for n in nums:
            total *= n
            prefix.append(total)
        return prefix

    def suffixProd(self, nums: List[int]) -> List[int]:
        suffix = []
        total = 1
        for n in reversed(nums):
            total *= n
            suffix.append(total)
        return suffix[::-1]