import random

print("welcome to dice roller basic!")
print("----------------------------")

#validate input
while True:
    try:
        faces= int(input('How any sides would you like your die to have? (max: 100) '))
        if (faces > 0 and faces <= 100):
            pass
        else:print("invalid input, please try again.")
        num_pick= int(input('How many dice would you like to roll? (max:10) '))
        if (num_pick > 0 and num_pick <= 10):
            break
        else:print("invalid input, please try again.")
    except:
        print("please provide an integer.")

def rollDice(amountofdice, faces):
    totalsum= 0
    #stores values for highest
    hidden_list = []
    possiblefaces = range(1 ,faces + 1)
    for die in range(amountofdice):
        roll = random.choice(possiblefaces)
        hidden_list.append(roll)
        print('Die', die + 1,": ", roll)
        totalsum += roll
    average = totalsum / amountofdice
    highest = max(hidden_list)
    print('Total: ', totalsum)
    print('Average: ', average)
    print('Highest: ', highest)

rollDice(num_pick, faces)