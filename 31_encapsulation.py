# 1. Using provate varibale inside class 

class student:
    __name="Rajat"            ## __name is private varibale whatever is starting from __ is private varibale can be used inside class
                              ##   and can be called also inside class only , cant be called through object, for more check notes


    def __init__(self):       # constructor
        print(self.__name)    # using private varibale in constructor

obj= student()               # Object instantiation, after this we cant call private variable and methods through objects



# 2. Using Private Mathods inside class

class student:
    __name="Rajat"            ## __name is private varibale whatever is starting from __ is private varibale can be used inside class
                              ##   and can be called also inside class only , cant be called through object, for more check notes


    def __init__(self):       # constructor
        print(self.__name)    # using private varibale in constructor
        self.__displayinfo()  # calling private method

    def __displayinfo(self):   # private methods same as provate varibale
        print("welcome Rajat")

obj= student()
