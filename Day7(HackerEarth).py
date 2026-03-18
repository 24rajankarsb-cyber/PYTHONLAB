# Roy and Profile Picture
# Problem
# Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.
# Minimum dimension of the picture can be L x L, where L is the length of the side of square.
# L = int(input())
# N = int(input())

# for x in range(N):
#     W, H = map(int, input().split())

#     if W < L or H < L:
#         print("UPLOAD ANOTHER")
#     elif W == H:
#         print("ACCEPTED")
#     else:
#         print("CROP IT")

# Result:
# input
# 180
# 3
# 640 480
# 120 300
# 180 180
# Output
# CROP IT
# UPLOAD ANOTHER
# ACCEPTED
# Expected Correct Output
# CROP IT
# UPLOAD ANOTHER
# ACCEPTED

# Monk and Rotation
# Problem
# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.
# T = int(input())

# for _ in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))

#     K = K % N

#     a1 = arr[:-K]   # first part
#     a2 = arr[-K:]   # last K elements

#     a3 = a2 + a1    # combine

#     print(*a3)

# Result:
# Input
# 1
# 5 2
# 1 2 3 4 5
# Output
# 4 5 1 2 3
# Expected Correct Output
# 4 5 1 2 3