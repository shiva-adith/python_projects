import random


while True:
    choice = input("Enter your choice or enter end to quit: ").lower()
    if choice == 'end':
        break

    choices = ['rock', 'paper', 'scissors']

    # the args for randint set the range required for the output.
    # the end value is inclusive and hence one is subtracted to prevent going out of index
    # computer_choice = choices[random.randint(0, len(choices)-1)]
    computer_choice = random.choice(choices)

    if choice in choices:
        if choice == computer_choice:
            print("It's a tie!")
        if choice == 'rock':
            if computer_choice == 'paper':
                print('You lost!')
            elif computer_choice == 'scissors':
                print("You beat the Computer!")

        if choice == 'paper':
            if computer_choice == 'scissors':
                print('You lost!')
            elif computer_choice == 'rock':
                print("You beat the Computer!")

        if choice == 'scissors':
            if computer_choice == 'rock':
                print('You lost!')
            elif computer_choice == 'paper':
                print("You beat the Computer!")
    else:
        print("Incorrect choice, please try again!\n")
        continue


    print('You chose: ', choice)
    print("The computer chose: ", computer_choice)
    print()
