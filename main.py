import random

print("welcome to dice roller basic!")
print("----------------------------")

#validate input
def valid_faces():
    while True:
        try:
            faces_input = int(input('How any sides would you like your die to have? (max: 100) '))
            if (faces_input > 0 and faces_input <= 100):
                return faces_input
            else:print("invalid input, please try again.")
        except:
            print("please provide an integer.")

def valid_pick():
     while True:
        try:
            num_pick= int(input('How many dice would you like to roll? (max:10) '))
            if (num_pick > 0 and num_pick <= 10):
                return num_pick
            else:print("invalid input, please try again.")
            
        except:
            print("please provide an integer.")

def get_bonus():
     while True:
        try:
            bonus_input = int(input('Bonus(applies to all die rolls): '))
            if bonus_input: 
                return bonus_input
        except:
            print("please provide an integer.")

def rollDice(amountofdice, faces, bonus):
    totalsum= 0
    #stores values for highest
    hidden_list = []
    possiblefaces = range(1 ,faces + 1)
    for die in range(amountofdice):
        roll = random.choice(possiblefaces)
        fin_roll = roll + bonus
        hidden_list.append(fin_roll)
        print('Die', die + 1,": ", fin_roll)
        totalsum += fin_roll
    average = totalsum / amountofdice
    highest = max(hidden_list)
    print('Total: ', totalsum)
    print('Average: ', average)
    print('Highest: ', highest)

faces = valid_faces()

amountofdice = valid_pick()

bonus = get_bonus()

rollDice(amountofdice, faces, bonus)