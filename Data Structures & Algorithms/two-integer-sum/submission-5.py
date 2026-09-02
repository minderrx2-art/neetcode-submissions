class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Ans = []
        for i, num in enumerate(nums):
            Ans.append((num,i))
        Ans.sort()
        i, j = 0, len(nums) - 1

        while True:
            left = Ans[i]
            right = Ans[j]
            if left[0] + right[0] == target:
                return sorted([left[1], right[1]])
            if left[0] + right[0] > target:
                j-=1
            else:
                i+=1