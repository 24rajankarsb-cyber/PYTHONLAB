# Palindrome No.
# class Solution:
#     def isPalindrome(self, x: int) -> bool:

#         if x < 0:
#             return False

#         s = str(x)

#         return s == s[::-1]

# Result :
# Input
# x =
# 121
# Output
# true
# Expected
# true

# Richest Customer Wealth
# class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     return max(map(sum, accounts))

# Result :
# Input
# accounts =
# [[1,2,3],[3,2,1]]
# Output
# 6
# Expected
# 6

# Find product
# MOD = 10**9 + 7

# # Read input
# n = int(input())
# arr = list(map(int, input().split()))

# # Compute product modulo MOD
# product = 1
# for num in arr:
#     product = (product * num) % MOD

# print(product)

# Result :
# Input
# 5
# 1 2 3 4 5
# Output
# 120
# Expected
# 120

# Staircase
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'staircase' function below.
# #
# # The function accepts INTEGER n as parameter.
# #

# def staircase(n):
#     # Write your code here
#      for i in range(1, n + 1):

#         print(" " * (n - i) + "#" * i)

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)

# Result :
# Input (stdin)
# 6
# Your Output (stdout)
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# Expected Output
#      #
#     ##
#    ###
#   ####
#  #####
# ######

# Minimum Maximum Sum
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def miniMaxSum(arr):
#     # Write your code here
#     total = sum(arr)

#     min_sum = total - max(arr)

#     max_sum = total - min(arr)

#     print(min_sum, max_sum)

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

# Result :
# Input (stdin)
# 1 2 3 4 5
# Your Output (stdout)
# 10 14
# Expected Output
# 10 14

# Birthday Cake Candles
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'birthdayCakeCandles' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY candles as parameter.
# #

# def birthdayCakeCandles(candles):
#     # Write your code here
#     tallest=max(candles)
#     count=candles.count(tallest)
#     return count

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     candles_count = int(input().strip())

#     candles = list(map(int, input().rstrip().split()))

#     result = birthdayCakeCandles(candles)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# Result :
# Input (stdin)
# 4
# 3 2 1 3
# Your Output (stdout)
# 2
# Expected Output
# 2

# Time Conversion
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #

# def timeConversion(s):
#     # Write your code here
#     hour = int(s[0:2])
#     minutes = s[3:5]
#     seconds = s[6:8]
#     period = s[8:10]

#     if period == "AM":
#         if hour == 12:
#             hour = 0
#     else:
#         if hour != 12:
#             hour += 12

#     return f"{hour:02}:{minutes}:{seconds}"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()

# Result :
# Input (stdin)
# 07:05:45PM
# Your Output (stdout)
# 19:05:45
# Expected Output
# 19:05:45