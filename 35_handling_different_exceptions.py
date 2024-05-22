# try:
#     a= int(input("enter a number : "))
#     c = 1/a
#     print(c)

# except Exception as e:
#     print("exception occured")
#     print(e)

# print("thanks for playing")

#test cases 
# 1. output can be like this

# enter a number : rajat
# exception occured
# invalid literal for int() with base 10: 'rajat'  # this is not error, it value of e which we have printed and it is handled so ti goes to next
# thanks for playing

# 2. 
# enter a number : 0
# exception occured
# division by zero      # divison by zero error but the code will flow without interruption thats y we use try and exception block
# thanks for playing     # here code will work without interruption

try:
    a= int(input("enter a number : "))
    c = 1/a
    print(c)

except ValueError as e:
    print("exception 1 occured")
    print(e)

except ZeroDivisionError as e:
    print("exception 2 occured")
    print(e)

print("thanks for playing")