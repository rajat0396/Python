#   *
#  ***
# *****     n=3


n=3
for i in range(n):
    print(" " * (n-i-1), end = " ")   # n-i-1 = 3-0-1 =2 means 2 spaces
    print("*" * (2*i+1),end = " ")    # end is a parameter of a print function 
    print(" " * (n-i-1))

# *
# ***
# *****

n=3
for i in range(n):
    print("*" * (2*i+1))