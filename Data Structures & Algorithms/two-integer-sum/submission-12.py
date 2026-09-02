class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # seen {4 => 1, 6 => 4}
        for i, v in enumerate(nums):
            prev = seen.get(v)
            if prev != None:
                return [prev, i]
            seen[target-v] = i
        return []