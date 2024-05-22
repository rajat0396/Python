# map.py  -- it is used when we want to use one function in all item

def square(num):
    return num*num

l=[1,2,3]
#method 1 - Normal method with map function
l2=[]
for item in l:
    l2.append(square(item))
print(l2)


# 2nd method by map function 

def sq(no):
    return no*no

l=[1,2,4]
print(list(map(square,l)))      # this is map function 


# filter function syntax   (list(filter(function,list_of_sequence)))

def greater_than_5(num):
    if num > 5:
        return True
    else: 
        False

l=[1,1,2,2,3,4,5,6,6,7,8,9]
print(tuple(filter(greater_than_5,l)))    # syntax with tuple
print(list(filter(greater_than_5,l)))     # syntax with list


# reduce function 
from functools import reduce

sum = lambda a,b:a+b
l=[1,2,3,4,5]
val = reduce(sum,l)
print(val)