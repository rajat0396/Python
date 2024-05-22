#write a program to print star patter

#         *  *  *
#         *     *
#         *  *  *            for n= 3


# ***   n=3      
# * *            
# ***            

n=3
for i in range(n):     # n will go from 0 to n-1 i.e 2
    if i==1:
        print("*" * (i),end = "")
        print(" " * (i),end = "")
        print("*" * (i))
    else:                    # when i =0 and 2 then we multiply * 3 times i.e n
        print("*" * (n))


n=3
for i in range(n):
    if i==1:
        print("*" * (i), end = " ")
        print(" " * (i), end = " ")
        print("*" * (i))
    else:
        print("* "* (n))


#      *
#     * *
#    *   *
#   *     *
#  *       *
# * * * * * *    n=4
        
n=6
for i in range(n):
    if i >0 and i<=n-2:
        print(" "*(n-i),end="")
        print("*",end="")
        print(" "*(2*i-1),end="")
        print("*",end="")
        print(" "*(n-i))
    else:
        print(" " * (n-i),end = "")
        print("*" * (2*i+1), end= "")
        print(" " * (n-i))

