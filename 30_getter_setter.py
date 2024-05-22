# getter and Setter in OOPS Python

class student:

    def __init__(self):
        self.__name=""
    
    def getname(self):
        return self.__name            
    
    def setname(self,name):
        self.__name=name                  # here we are stting the vale

obj = student()                           # object instantiation
obj.setname("testing")                    # value set
name= obj.getname()                       # get value
print(name)


'''decoding
first we set the name "Testing " in name and then it is assigned to variable self.__name
then we have to get the value and its now return self.__name and that have "Testing" in it and it returns that  '''