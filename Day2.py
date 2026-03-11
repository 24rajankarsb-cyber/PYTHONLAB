# no=int(input("Enter the no:"))
# rev=0
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
#     no=no//10
# print("Reverse no is",rev)

# no=int(input("Enter the no:"))
# sum=0
# while no>0:
#     rem=no%10
#     sum=sum+rem
#     no=no//10
# print("Sum of digits is",sum)

# no=int(input("Enter the no:"))
# count=0
# while no>0:
#     rem=no%10
#     count=count+rem
#     no=no//10
# print("Number of digits is",count)

for i in range(1,1000):
    no=i
    count=0
    sum=0
    temp=no

    while no>0:
        rem=no%10
        sum=sum+rem**count
        no=no//10

        if temp==sum:
            print(temp,"is armstrong no")
