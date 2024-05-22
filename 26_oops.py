class Number:               # class syntex in PascalCase
    a=10                    # class varibale
    b=20

num=Number()     # Number is class , num is object variable and together they are known as object
print("the sum of a and b is ", num.a + num.b)



# calling function through object

class DemoClass:
    a=10
    def sumvalue(self):
        print(10+20)

demoobject=DemoClass()
print(demoobject.a)
demoobject.sumvalue()
