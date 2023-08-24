import random


def rollDice(amountOfDice, sidesOfDice):
    totalSum = 0
    for die in range(amountOfDice):
        roll = random.randint(1, sidesOfDice)
        print("Die ", die + 1, ": ", roll)
        totalSum += roll
    print("Total sum: ", totalSum)

print("Welome to my DnD Dice Roller")
print("----------------------------")

### Validate input

validate=True


while validate:
    try:
        sidePick = int(input("Choose the number of sides: "))
        if(sidePick == 0):
            break
        numberPicked = int(input("Type an integer between 1 and 20 for the amount of dice rolled: "))
        if(numberPicked > 0 and numberPicked < 21):
            rollDice(numberPicked, sidePick)
        else:
            print("Invalid Input. Try again.")
    except:
        print("Please provide an integer")