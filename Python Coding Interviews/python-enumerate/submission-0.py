from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i,num in enumerate(nums):
        if num == 7:
            return i
    return -1

def get_dist_between_sevens(nums: List[int]) -> int:
    num1, num2 = -1,-1
    for i,num in enumerate(nums):
        if num1 == -1 and num == 7:
            num1 = i
        elif num2 == -1 and num == 7:
            num2 = i
    return num2 - num1
# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
