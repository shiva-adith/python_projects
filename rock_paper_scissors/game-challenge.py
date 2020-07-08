import random


while True:
    choice = input("Enter your choice or enter end to quit: ").lower()
    if choice == 'end':
        break

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    choices_dict = {'rock' : 0, 'paper' : 1, 'scissors' : 2}
    choices_index = choices_dict.get(choice, 3)
    print("Choice Index: ",choices_index)



    print('You chose: ', choice)
    print("The computer chose: ", computer_choice)
    print()
