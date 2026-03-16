# # Complete the compareTriplets function below.
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def compareTriplets(a, b):
#     alice = 0
#     bob = 0

#     for i in range(3):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1

#     return [alice, bob]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

# Very Big Sum

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'aVeryBigSum' function below.
# #

# def aVeryBigSum(ar):
#     total = 0
#     for i in ar:
#         total = total + i
#     return total

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# Diagonal Difference
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# # # # Complete the 'diagonalDifference' function below.
# #
# def diagonalDifference(arr):
#     left_diagonal = 0
#     right_diagonal = 0

#     for i in range(len(arr)):
#         left_diagonal += arr[i][i]
#         right_diagonal += arr[i][len(arr) - 1 - i]

#     return abs(left_diagonal - right_diagonal)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# Plus Minus array
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# def plusMinus(arr):
#     pos = 0
#     neg = 0
#     zero = 0
#     n = len(arr)

#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i < 0:
#             neg += 1
#         else:
#             zero += 1

#     print("{:.6f}".format(pos/n))
#     print("{:.6f}".format(neg/n))
#     print("{:.6f}".format(zero/n))

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)












