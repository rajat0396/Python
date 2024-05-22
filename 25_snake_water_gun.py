# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.

import random
# Snake Water Gun or Rock Paper Scissors

def gamewin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
        
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        if you =='w':
            return True
        
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True

# print computer turn input        
print("Computer Turn : Snake(s) Water(w) or Gun(g)?")

# give random varibale form 1 to 3 and declare a variable randNO if randNo ==1 then computer will choose s and son on
randNo= random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
# yours input    
you = input("your turn Snake(s) Water(w) or  Gun(g)? ")
a = gamewin(comp, you)                                       # calling function


# printing computer and your turn
print(f"computer turn is {comp}")
print(f"yours turn is {you}")

# if retrun value is none when both computer an you have given same value then its tie

if a == None:
    print("game is tie!")                
elif a:
    print("You Win ! ")               # when a is ture you win
else:
    print("you Loose! ")              # when a is false you loose

        