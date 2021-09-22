import field

def user_input(player):
    while True:
        i = input(f'Type in the coordinate where to place your {player}:').upper()
        if len(i) != 2:
            print('Theres something wrong in your input. Please try again.')
            continue
        x = i[0]
        y = i[1]
        if x != 'A' and x != 'B' and x != 'C' and y != '1' and y != '2' and y != '3':
            print('This coordinate doesn\'t exist. Please try again.')
            continue
        
        return i

def update_field(putin, player):
    field.field[putin] = player

def check_if_game_won(p):
    pass
    
            
def game_loop():
    rematch = True
    while(rematch):
        # set counter which determines which player
        move = 0
        # counter up
        move = move + 1
        # print field
        field.draw_field()
        # determine player with counter
        player = 'X' if move % 2 != 0 else 'O'
        # ask for input
        putin = user_input(player)
        # set input in dictionary
        update_field(putin, player)
        # detemine if game is won
        if move > 4:
            check_if_game_won(player)
        # ask for rematch if one
        rematch = True if input('Do you want a rematch? Press y for yes.') == 'y' else False
        
game_loop()