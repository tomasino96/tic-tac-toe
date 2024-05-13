player1 = 'x'
player2 = 'o'

current_player = 1

run = True

field_xy = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def print_field():
    for i in field_xy:
        for j in i:
            print(j, end="")
        print()

def player_move(player):
    check = False

    while not check:
        x = int(input("Choose row: "))
        y = int(input("Choose column: "))

        if field_xy[x - 1][y - 1] != "_":
            print("Error: Spot already taken. Choose another spot.")
        else:
            field_xy[x - 1][y - 1] = player
            check = True

def check_for_rows(player):
    global run
    for i, row in enumerate(field_xy):
        if row == [player, player, player]:
            print(f"Player {current_player} won(row)")
            print_field()
            run = False

def check_for_columns(player):
    global run
    for i in range(3):
        if field_xy[0][i] == field_xy[1][i] == field_xy[2][i] == player:
            print(f"Player {current_player} won(column)")
            print_field()
            run = False

def check_for_diagonals(player):
    global run
    if field_xy[0][0] == field_xy[1][1] == field_xy[2][2] == player:
        print(f"Player {current_player} won(diagonal)")
        print_field()
        run = False
    elif field_xy[0][2] == field_xy[1][1] == field_xy[2][0] == player:
        print(f"Player {current_player} won(diagonal)")
        print_field()
        run = False

def check_for_space():
    global run
    space = 0
    for i in field_xy:
        for j in i:
            if j != "_":
                space = space + 1
                if space == 9:
                    print("Tie")
                    run = False
    
#main code
while run:
    current_player = 1
    print(f"Player 1 is playing [{player1}]")

    print_field()

    player_move(player1)
    check_for_rows(player1)
    check_for_columns(player1)
    check_for_diagonals(player1)
    check_for_space()

    if not run:
        break

    current_player = 2
    print(f"Player 2 is playing [{player2}]")

    print_field()

    player_move(player2)
    check_for_rows(player2)
    check_for_columns(player2)
    check_for_diagonals(player2)
    check_for_space()

