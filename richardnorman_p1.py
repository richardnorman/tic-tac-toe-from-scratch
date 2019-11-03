import richardnorman_p1_drawing
import stddraw
import global_variables_p1
    
def check_if_tie():
    tie = True
    #if there is still a 0 in the 2d array(no marker present), game is not tied yet
    for i in range (3):
        for j in range (3):
            if global_variables_p1.marker_array[j][i] == 0:
                tie = False
    if tie:
        richardnorman_p1_drawing.draw_tie()
    return tie

def check_if_player_won(turn_number):
    global game_won

    #check rows
    for i in range (3):
        if global_variables_p1.marker_array [i][0] == 1 and global_variables_p1.marker_array [i][1] == 1 and global_variables_p1.marker_array [i][2] == 1:
            #row has all X
            game_won = True
        if global_variables_p1.marker_array [i][0] == 2 and global_variables_p1.marker_array [i][1] == 2 and global_variables_p1.marker_array [i][2] == 2:
            #row has all O
            game_won = True
    
    #check columns
    for j in range(3):
        if global_variables_p1.marker_array [0][j] == 1 and global_variables_p1.marker_array [1][j] == 1 and global_variables_p1.marker_array [2][j] == 1:
            #column has all X
            game_won = True
        if global_variables_p1.marker_array [0][j] == 2 and global_variables_p1.marker_array [1][j] == 2 and global_variables_p1.marker_array [2][j] == 2:
            #xolumn has all O
            game_won = True
    
    #check diagonals
    if global_variables_p1.marker_array [0][0] == 1 and global_variables_p1.marker_array [1][1] == 1 and global_variables_p1.marker_array [2][2] == 1:
        #diagonal from top left to bottom right has all X
        game_won = True
    if global_variables_p1.marker_array [0][0] == 2 and global_variables_p1.marker_array [1][1] == 2 and global_variables_p1.marker_array [2][2] == 2:
        #diagonal from top left to bottom right has all O
        game_won = True
    if global_variables_p1.marker_array [2][0] == 1 and global_variables_p1.marker_array [1][1] == 1 and global_variables_p1.marker_array [0][2] == 1:
        #diagonal from bottom left to top right has all X
        game_won = True
    if global_variables_p1.marker_array [2][0] == 2 and global_variables_p1.marker_array [1][1] == 2 and global_variables_p1.marker_array [0][2] == 2:
        #diagonal from bottom left to top right has all O
        game_won = True

    if game_won:
        richardnorman_p1_drawing.draw_win(turn_number)

global_variables_p1.init()

turn_number = 1
richardnorman_p1_drawing.draw_board()
game_won = False

richardnorman_p1_drawing.draw_turn(turn_number)

while not game_won:
    if stddraw.mousePressed():
        valid_placement = richardnorman_p1_drawing.draw_piece(stddraw.mouseX(),stddraw.mouseY(),turn_number)
        if not valid_placement:
            continue
        check_if_player_won(turn_number)
        if game_won:
            break
        is_tie = check_if_tie()
        if is_tie:
            break
        turn_number += 1
        richardnorman_p1_drawing.draw_turn(turn_number)
    stddraw.show(0.0)