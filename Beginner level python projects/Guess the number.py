import random

def guessnum(x):
    n=random.randint(1,10)
    g=0
    while n != g:
        g=int(input(f"Enter a number between 1 and {x}: "))
        if g<n:
            print("Sorry!!! guess the number again.....Too low :'( ")
        elif g>n:
            print("Sorry!!! guess the number again.....Too high :'( ")     
    print("Congratulations!!! You guess the right number")

guessnum(10)