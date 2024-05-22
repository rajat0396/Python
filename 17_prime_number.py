# give number is prime or not

num=int(input("enter any number"))
prime = True
for i in range(2,num):
    if(num%i==0):
        prime = False
        break
if prime:
    print("number is prime")
else:
    print("number is not prime")