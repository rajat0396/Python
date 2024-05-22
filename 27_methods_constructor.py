class DemoClass:
    a=10
    def showvalue(self):
        self.c=self.a*self.a   # in function if we want to define and variable or print any variable we use self
        print(self.c)          # self is like an object it can call class variable also.

    def showvalue1(self):            # and we can make multiple methods also
        print("welcome  rajat")
    

obj=DemoClass()
obj.showvalue()
obj.showvalue1()




# multiple argument
class DemoClass:
    a=10
    def showvalue(self):
        self.c=self.a*self.a   # in function if we want to define and variable or print any variable we use self
        print(self.c)          # self is like an object it can call class variable also.

    def showvalue1(self,a,b):            # and we can make multiple methods also
        print(a*b)                       # other then self argumentm which we are defining we need not use self for that
                                         # i.e we have define when we call function

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)


# defining constructor  

class DemoClass:
    a = 10
    def __init__(self):                          # construction is also defined as same function but with keyword init and underscore and use self also here
        print("welcome rajat : to learn OOPS")   # for constructor we dont need to call it get automatically called

    def showvalue(self):
            self.c=self.a*self.a                 # in function if we want to define and variable or print any variable we use self
            print(self.c)                        # self is like an object it can call class variable also.

    def showvalue1(self,a,b):                # and we can make multiple methods also
            print(a*b)                           # other then self argumentm which we are defining we need not use self for that
                                                 # i.e we have define when we call function

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)


