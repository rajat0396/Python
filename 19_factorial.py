#write a program to find the factorial number

num=int(input("enter any number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i

print("the factorial of number is:  ", factorial )