class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1

        while True:
            sum = numbers[i] + numbers[j]
            match sum:
                case n if n > target:
                    j-=1
                case n if n < target:
                    i+=1
                case n if n == target:
                    return [i+1,j+1]