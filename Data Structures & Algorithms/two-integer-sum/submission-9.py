class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            comp[target - num] = i
        for i, num in enumerate(nums):
            if comp.get(num) and comp.get(num) != i:
                return [i, comp.get(num)]