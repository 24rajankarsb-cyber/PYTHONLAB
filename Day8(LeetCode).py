# TWO SUM
# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = {}  # Dictionary to store value -> index
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i

# Fizz Buzz
# from typing import List

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         result = []

#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))

#         return result

# Runnimg Sum of 1d Array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1,len(nums)):
#             nums[i]=nums[i]+nums[i-1]
#         return nums
