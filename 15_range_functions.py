for i in range(5):   # by defualt it start from 0 to n-1
    print(i)

# if we want it to be start from 1 then

for i in range(1,8):
    print(i)

# step size uses

for i in range(1,10,3):   #3 is step size means 2 no will be cutted 
                          #i.e 1 will be printed then 2 and 3 wont be there ,
                          # then 4 printed , 5and 6 wont be there , then 7 printed
    print(i)

for i in range(1,5,1):
    print(i)

#else with for loop
    
for i in range(5):
    print(i)
else:
    print("this else is inside for loop")    # this else loop executes when i becomes for loop becomed false
                                             # i.e i start from 0 and will go to n-1 i.e 5-1=4 , fir jaise he condition
                                             # false huyi , jab i =5 hua then it came in else loop

# break statement

for i in range(1,6):
    print(i)
    if i == 3:   # jab i ki value =3 ho jaygi i will break and come out of the for loop
        break
else:               # this else statement will be printed then only if for loop is successfully terminated 
                    # here it is because of break statement i.e not successfully terminated so it wont print
    print("done")

# continue statement

for i in range(1,7):
    print(i)
    if i == 4:
        continue
    