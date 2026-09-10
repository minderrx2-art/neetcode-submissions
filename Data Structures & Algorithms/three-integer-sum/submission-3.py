class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                if l != i+1 and nums[l-1] == nums[l]:
                    l+=1
                    continue
                match nums[l] + nums[r] + a:
                    case n if n > 0:
                        r -= 1
                        continue
                    case n if n < 0:
                        l += 1
                        continue
                    case n if n == 0:
                        res.append([a,nums[l], nums[r]])
                l+=1
                r-=1
        return res