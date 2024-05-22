# # write a program to find greatest of three numbers

# a = int(input())
# b = int(input())
# c = int(input())

# if (a>b and a > c):
#     print("a is greatest")
# if(b > a and b > c):
#     print(" b is greatest")
# else:
#     print("c is greatest")

# # using function:
    
# def greater(a,b,c):
#     if (a>b and a > c):
#         return a
#     if(b > a and b > c):
#          return b
#     else:
#         return c

# a = int(input())
# b = int(input())
# c = int(input())
# s = greater(a,b,c)
# print("the greater no is ", s)


# using recursive sum of first n natural number
# first n sum = n + (n-1)

def first_n_sum_recursive(n):
    if n == 0:
        return 0
    return n +first_n_sum_recursive(n-1)

s=first_n_sum_recursive(4)
print("the sum of first five no is ", str(s))

