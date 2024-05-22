# program to calculate percentage by sum function and without sum function i.e manually

marks = [45,76,78,89]
percentage1=(sum(marks)/400)*100    # we used sum function if we dont know sum function the we can write marks[0]+marks[1] and son on

marks2 = [47,71,88,69]
percentage2=((marks2[0] +marks2[1] +marks2[2] +marks2[3])/400)*100

print(percentage1)
print(percentage2)

# similarly if we have 10 list of marks ,marks1 , marks2, marks3 and so on  and we have to find percentage then we can write the function

def percent(marks):                                                  # def is a keyword to define a function
  # we made a function by name percent(marks) and taken marks in function   and percent() we can write like this also 
  # it means it is not taking and values , but here we are taking input as marks
    return((marks[0] +marks[1] +marks[2] +marks[3])/400)*100         # here it will return the marks perntage
    # return is also a keyword

marks1 = [45,76,78,89]
percentage1=percent(marks1)         # now when we call marks1 , it will copy into this percentage(marks) function and in this 
#  function whatever we are ruturning will copy in place of percent(marks)

marks2 = [47,71,88,69]
percentage2=percent(marks2)         # whatever is returning from function

print(percentage1)
print(percentage2)