while (True):
    print("Press q to quit")
    a = input("enter the number : ")
    if a == 'q':
        break
    a= int(a)
    if a > 6:
        print (" the number is greater then 6 ")

print("thanks for playing")


# using try and exception it will give you an error in good way

while (True):
    print("Press q to quit")
    a = input("enter the number : ")
    if a == 'q':
        break
    try:                                         # try block 
        a= int(a)
        if a > 6:
            print (" the number is greater then 6 ")
    except Exception as e:                                  # exception block willl give you an error and will print an e here
        print(e)

print("thanks for playing")    
    
