# # single inheritance

class A:
    def showvalueA(self):
        print("wlecome Rajat A")
    
class B(A):            # class A inherits into class B
    def showvalueB(self):
        print("welcome Rajat B")

obj=B()  # will make object from class B , that can call methods of class A and class B
obj.showvalueA()
obj.showvalueB()


# Multilevel inheritance : when child class becomes parent  class of another chil class:

class A:
    def showvalueA(self):
        print("wlecome Rajat A")
    
class B(A):            # class A inherits into class B
    def showvalueB(self):
        print("welcome Rajat B")

class C(B):           # class B inherits into class C
    def showvalueC(self):
        print("welcome rajat C")

obj=C()  # will make object from class C , that can call methods of class A and class B, and class C
obj.showvalueA()
obj.showvalueB()
obj.showvalueC()

# Mulitple Inheritance:

class A:                               # 1st parent class 
    def showvalueA(self):
        print("wlecome Rajat A")
    
class B:                                # 2nd Parent Class
    def showvalueB(self):
        print("welcome Rajat B")

class C(A,B):           # class A and B inherits into class C
    def showvalueC(self):
        print("welcome rajat C")

obj=C()  # will make object from class C , that can call methods of class A and class B, and class C
obj.showvalueA()
obj.showvalueB()
obj.showvalueC()

