class DemoClass:
    a = 10
    def __init__(self):                          
        print("welcome rajat : to learn OOPS")   

    def showvalue(self):
            self.c=self.a*self.a             
            print(self.c)                       
    def showvalue1(self,d,e):          
            print(d*e)                        
                                                
d=20
e=30
obj=DemoClass()
obj.showvalue()

obj.showvalue1(d,e)