# factorial using recursion

# n! = 1*2*3.....*n

# without recursion

n=5
product=1
for i in range(n):
    product = product*(i+1)

print(product)

# using function with for loop

def factorial_itr(n):
    product=1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial_itr(5)
print(f)

#factorial_recursive

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

print(n)
f = factorial_recursive(5)
print(f)