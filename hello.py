import random
selectedNumber=random.randint(1,20)
print("I am thinking of a number between 1 and 20.There are 6 guesses for you")
for i in range(7):
    if i>6:
        print("Sorry you lost your chances")
    else:
        print("Take a guess")
        inputNumber=int(input())
        if inputNumber<selectedNumber:
            print("Value is too low")
        elif inputNumber>selectedNumber:
            print("Value is too high")
        else:
            print("Good job! You guessed my number in ",str(int(i)+1),"guesses!")
            break
    
