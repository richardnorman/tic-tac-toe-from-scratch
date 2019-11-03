import stddraw
import global_variables_p1

stddraw.setCanvasSize(450,450)
stddraw.setFontSize(24)
def draw_board():
    stddraw.line((1/3),1,(1/3),0)
    stddraw.line((2/3),1,(2/3),0)
    stddraw.line(0,(2/3),1,(2/3))
    stddraw.line(0,(1/3),1,(1/3))

def draw_tie():
    stddraw.text((1/3) + (1/3)/2,0.98,"TIED GAME!")
    stddraw.show()

def draw_win(turn_number):
    if turn_number % 2 == 0:
        #player two won
        stddraw.text((1/3) + (1/3)/2,0.98,"PLAYER 2 WON!")
    else:
        #player one won
        stddraw.text((1/3) + (1/3)/2,0.98,"PLAYER 1 WON!")
    stddraw.show()

def draw_turn(turn_number):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0.96,80,20)
    stddraw.setPenColor(stddraw.BLACK)
    if turn_number % 2 != 0:
        stddraw.text((1/3)/2,0.98,"Player 1's Turn")
    else:
        stddraw.text((1/3)/2,0.98,"Player 2's Turn")

def draw_marker(x,y,turn_number):
    if turn_number % 2 != 0:
        #player one clicked
        #draw an X
        stddraw.line(x + 0.1, y + (1/3) - 0.1, x + (1/3) - 0.1, y + 0.1)
        stddraw.line(x + 0.1, y + 0.1, x + (1/3) - 0.1, y + (1/3) - 0.1)
    else:
        #player two clicked
        #draw an O
        stddraw.circle(x + (1/3)/2, y + (1/3) - (1/3)/2,0.1)

def draw_piece(x,y,turn_number):
    if (0 < x < (1/3)) and ((2/3) < y < 1):
        #top left
        #check if spot is already occupied
        if global_variables_p1.marker_array[0][0] != 0:
            #spot occupied, dont draw
            return False
        draw_marker(0,(2/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[0][0] = 1
        else:
            global_variables_p1.marker_array[0][0] = 2
        return True
    if ((1/3) < x < (2/3)) and ((2/3) < y < 1):
        #top middle
        #check if spot is already occupied
        if global_variables_p1.marker_array[0][1] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((1/3),(2/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[0][1] = 1
        else:
            global_variables_p1.marker_array[0][1] = 2
        return True
    if ((2/3) < x < 1) and ((2/3) < y < 1):
        #top right
        #check if spot is already occupied
        if global_variables_p1.marker_array[0][2] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((2/3),(2/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[0][2] = 1
        else:
            global_variables_p1.marker_array[0][2] = 2
        return True

    if (0 < x < (1/3)) and ((1/3) < y < (2/3)):
        #middle left
        #check if spot is already occupied
        if global_variables_p1.marker_array[1][0] != 0:
            #spot occupied, dont draw
            return False
        draw_marker(0,(1/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[1][0] = 1
        else:
            global_variables_p1.marker_array[1][0] = 2
        return True
    if ((1/3) < x < (2/3)) and ((1/3) < y < (2/3)):
        #center
        #check if spot is already occupied
        if global_variables_p1.marker_array[1][1] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((1/3),(1/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[1][1] = 1
        else:
            global_variables_p1.marker_array[1][1] = 2
        return True
    if ((2/3) < x < 1) and ((1/3) < y < (2/3)):
        #middle right
        #check if spot is already occupied
        if global_variables_p1.marker_array[1][2] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((2/3),(1/3),turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[1][2] = 1
        else:
            global_variables_p1.marker_array[1][2] = 2
        return True

    if (0 < x < (1/3)) and (0 < y < (1/3)):
        #bottom left
        #check if spot is already occupied
        if global_variables_p1.marker_array[2][0] != 0:
            #spot occupied, dont draw
            return False
        draw_marker(0,0,turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[2][0] = 1
        else:
            global_variables_p1.marker_array[2][0] = 2
        return True
    if ((1/3) < x < (2/3)) and (0 < y < (1/3)):
        #bottom middle
        #check if spot is already occupied
        if global_variables_p1.marker_array[2][1] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((1/3),0,turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[2][1] = 1
        else:
            global_variables_p1.marker_array[2][1] = 2
        return True
    if ((2/3) < x < 1) and (0 < y < (1/3)):
        #bottom right
        #check if spot is already occupied
        if global_variables_p1.marker_array[2][2] != 0:
            #spot occupied, dont draw
            return False
        draw_marker((2/3),0,turn_number)
        if turn_number % 2 != 0:
            global_variables_p1.marker_array[2][2] = 1
        else:
            global_variables_p1.marker_array[2][2] = 2
        return True
