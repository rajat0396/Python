#same function i.e length different signature i.e different data types, list and string is polymorphism
l=[10,20,30,40]
print(len(l))

s="welcome"
print(len(s))

# function overloading

class WS:
    def displayinfo(self):
        name=""
        print("welcome" + name)

obj=WS()
obj.displayinfo()        # here we have not passed parameter, if we have pass paramter also then also it will work just see below eg


class WS:
    def displayinfo(self,name=''):
        print("welcome" + name)

obj=WS()
obj.displayinfo()  # Here we have pass paramter
obj.displayinfo('Rajat')

# Overloading same function name but we can give different paramter accordingly

# Function Overriding
# i.e same function name and then function over ride after inherits, but it should be different class

class WS:
    def displayinfo(self):
        print("Welcome")

class IIP(WS):      # class inherits
    def displayinfo(self):          # same function name
        print("Welcome Rajat")

obj=IIP()           # obj instantiation of inherits
obj.displayinfo()


# Super function i.e we can call parent function of the same name in child class/child fucntion

class WS:
    def displayinfo(self):
        print("Welcome")

class IIP(WS):      # class inherits
    def displayinfo(self):          # same function name
        super().displayinfo()          # super function calling parent function 
        print("Welcome Rajat")

obj=IIP()           # obj instantiation of inherits
obj.displayinfo()