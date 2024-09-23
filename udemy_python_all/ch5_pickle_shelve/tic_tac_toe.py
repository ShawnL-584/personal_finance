counter = 0
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    choice = input('Please enter a number(1-9) :')
    while not choice.isdigit() or int(choice) not in range(1, 10):
        if not choice.isdigit():
            print('Sorry, your choice is not valid.')
        else:
            print('Your choice is not within the range 1 - 9.')
        choice = input('Please enter a number(1-9) :')
    return int(choice)


def getCurrentSymbol():
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list[counter % 2]


def update_table(index):
    if index in range(1, 4):
        if row1[index - 1] == ' ':
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index - 4] == ' ':
            row2[index - 4] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(7, 10):
        if row3[index % 3 - 1] == ' ':
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False


def check_winning():
    player1_wins = False
    player2_wins = False
    if (row1[0] == row1[1]) and (row1[1] == row1[2]) and (' ' not in row1):
        if row1[0] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row2[0] == row2[1]) and (row2[1] == row2[2]) and (' ' not in row2):
        if row2[0] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row3[0] == row3[1]) and (row3[1] == row3[2]) and (' ' not in row3):
        if row3[0] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row1[0] == row2[0]) and (row2[0] == row3[0]) and (row1[0] != ' ' and row2[0] != ' ' and row3[0] != 0):
        if row1[0] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row1[1] == row2[1]) and (row2[1] == row3[1]) and (row1[1] != ' ' and row2[1] != ' ' and row3[1] != 0):
        if row1[1] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row1[2] == row2[2]) and (row2[2] == row3[2]) and (row1[2] != ' ' and row2[2] != ' ' and row3[2] != 0):
        if row1[2] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row1[0] == row2[1]) and (row2[1] == row3[2]) and (row1[0] != ' ' and row2[1] != ' ' and row3[2] != 0):
        if row1[0] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    elif (row1[2] == row2[1]) and (row2[1] == row3[0]) and (row1[2] != ' ' and row2[1] != ' ' and row3[0] != 0):
        if row1[2] == 'O':
            player1_wins = True
        else:
            player2_wins = True
    if player1_wins:
        return 'player 1 wins'
    elif player2_wins:
        return 'player 2 wins'
    else:
        return 'no one wins'


def start_game():
    while True:
        display(row1, row2, row3)

        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print('Wrong position to put your choice.')
        result = check_winning()
        if result == 'player 1 wins':
            display(row1, row2, row3)
            print('Player 1 wins. Congrats!!!')
            return
        elif result == 'player 2 wins':
            display(row1, row2, row3)
            print('Player 2 wins. Congrats!!!')
            return
        elif result == 'no one wins' and counter == 9:
            display(row1, row2, row3)
            print('Tie game.')
            return


start_game()
