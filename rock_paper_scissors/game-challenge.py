import random


while True:
    user_choice = input("Enter your choice or enter end to quit: ").lower()
    if user_choice == 'end':
        break

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    choices_dict = {'rock' : 0, 'paper' : 1, 'scissors' : 2}

    # Returns the index of the user's choice.
    # If choice isn't in the dict, index is defaulted to 3.
    user_index = choices_dict.get(user_choice, 3)

    # comp index doesn't need a default val. since it makes only valid choices.
    computer_index = choices_dict.get(computer_choice)
    # print("Choice Index: ",choices_index)

    """
        Results Matrix:
            Key =  0:TIE; 1:WIN; 2:LOSE; 3:INVALID
                           Computer choices:
                     ---------------------------
        User Choices |  Rock | Paper | Scissors|
        ---------------------------------------
            Rock     |   0   |   2   |    1    |
                     --------------------------
            Paper    |   1   |   0   |    2    |
                     --------------------------
            Scissors |   2   |   1   |    0    |
                     --------------------------
            Invalid  |   3   |   3   |    3    |
        ----------------------------------------
    """

    results_matrix = [[0, 2, 1],
                      [1, 0, 2],
                      [2, 1, 0],
                      [3, 3, 3]]

    results_index = results_matrix[user_index][computer_index]

    results_messages = dict([(0,"Its a Tie! ^--(o.o)--^"),(1, "You beat the Computer! |__[*o*]__|"), (2, "You lost {O_O}"), (3, "Invalid choice, try again! ->(o_O)<-")])

    print('You chose: ', user_choice)
    print("The computer chose: ", computer_choice)
    print("Result: ", results_messages.get(results_index))
    print()
