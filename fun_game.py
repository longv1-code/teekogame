
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Long Vo
#               Bradley Sun
#               Liam Searing
#
# Section:      519
# Assignment:   13: Fun Game
# Date:         12/2/23
import turtle


f = open("instructions.txt", "w")
f.write("The Teeko board consists of twenty-five spaces arranged in a five-by-five grid. \nThere are eight markers in a Teeko game, four black and four red. \nOne player, \"Black\" plays the black markers, and the other, \"Red\", plays the red. \nBlack moves first and places one marker on any space on the board. \nRed then places a marker on any unoccupied space; black does the same; and so on until all eight markers are on the board. \nThe object of the game is for either player to win by having all four of their markers in a straight line (vertical, horizontal, or diagonal) \nor on a square of four adjacent spaces. (Adjacency is horizontal, vertical, or diagonal, but does not wrap around the edges of the board.) \nIf neither player has won after the \"drop\" (when all eight pieces are on the board), then they move their pieces one at a time, with Black playing first. \nA piece may be moved only to an adjacent space.")
f.close()




def readInstructions():
    a = open("instructions.txt")
    lines = a.readline()
    while lines:
        print(lines, end="")
        lines = a.readline()
    a.close()
#Display rules code
def DisplayRules():
   print("You win by getting all four of your dots in a straight line (horizontal, vertical, or diagonal) or making a 2x2 square \nFirst turn is black. You take turns placing either or black or red dots; Once 4 of each dot have been placed, you stop \nplacing new dots and start moving the ones already placed only adjacent to the original position")


#Turtle Set-up
turtle.home()
turtle.position()
(0.00,0.00)
t = turtle.Turtle(visible=False)
turtle.setup(360,360)
turtle.penup()
def board_reset():
    turtle.Screen()
    turtle.penup()
    turtle.setheading(270)
    for i in range(0,360,60):
        turtle.goto(i-150,150)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()
    turtle.setheading(0)
    for i in range(0,360,60):
        turtle.goto(-150,i-150)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()


def red_dot(row,column): #Places a red piece
    turtle.Screen()
    turtle.penup()
    turtle.goto((row-3)*60,(3-column)*60)
    turtle.dot(40,"red")


def black_dot(row,column): #Places a black piece
    turtle.Screen()
    turtle.penup()
    turtle.goto((row-3)*60,(3-column)*60)
    turtle.dot(40,"black")


def erase_dot(row,column): #Erases the dot in a space
    turtle.Screen()
    turtle.penup()
    turtle.goto((row-3)*60,(3-column)*60)
    turtle.dot(42,"white")


BoardList = [[" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]]


def HorizontalWin(char):
   counter = 0
   for i in BoardList:
       for j in i:
           if j == char:
               counter += 1
           else:
               counter = 0
           if counter == 4:
               return True
       counter = 0
   return False




def VerticalWin(char):
   counter = 0
   for i in range(5):
       for j in range(5):
           if BoardList[j][i] == char:
               counter += 1
           else:
               counter = 0
           if counter == 4:
               return True
       counter = 0
   return False




def DiagonalWin(char):
   if (BoardList[0][0] == char and BoardList[1][1] == char and BoardList[2][2] == char and BoardList[3][3] == char):
       return True
   elif (BoardList[4][4] == char and BoardList[1][1] == char and BoardList[2][2] == char and BoardList[3][3] == char):
       return True
   elif (BoardList[1][0] == char and BoardList[2][1] == char and BoardList[3][2] == char and BoardList[4][3] == char):
       return True
   elif (BoardList[0][1] == char and BoardList[1][2] == char and BoardList[2][3] == char and BoardList[3][4] == char):
       return True
   elif (BoardList[4][0] == char and BoardList[3][1] == char and BoardList[2][2] == char and BoardList[1][3] == char):
       return True
   elif (BoardList[0][4] == char and BoardList[3][1] == char and BoardList[2][2] == char and BoardList[1][3] == char):
       return True
   elif (BoardList[3][0] == char and BoardList[2][1] == char and BoardList[1][2] == char and BoardList[0][3] == char):
       return True
   elif (BoardList[4][1] == char and BoardList[3][2] == char and BoardList[2][3] == char and BoardList[1][4] == char):
       return True
   else:
       return False




def SquareWin(char):
   # Assume 'my_array' is defined in the outer scope
   for i in range(4):  # Rows
       for j in range(4):  # Columns
           # Extract the 2x2 square
           square = [
               [BoardList[i][j], BoardList[i][j + 1]],
               [BoardList[i + 1][j], BoardList[i + 1][j + 1]]
           ]
           if (char in square[0][0]) and (char in square[0][1]) and (char in square[1][0]) and (char in square[1][1]):
               return True
   return False




def WinCondition(char):
    if SquareWin(char):
       return True
    elif HorizontalWin(char):
       return True
    elif VerticalWin(char):
       return True
    elif DiagonalWin(char):
       return True
    return False




def turn_text():
    print(f"---It is now {player}'s turn. What will you like to do?")
    print("\u0332".join("Type \"instructions\" to display the instructions."))
    print("\u0332".join("Type \"rules\" to display the rules of the win condition."))
    print("\u0332".join("Type \"end\" to end the game early."))
    print("\u0332".join("Type \"move\" to do your move."))


turn_count = 0
def place_piece(color):
    global turn_count
    turn_active = True
    turn_count += 1
    print("Please select a row and column to place your piece:")
    while turn_active:
        row=int(input("Row (1-5):"))
        column=int(input("Column (1-5):"))
        if BoardList[row-1][column-1] == " ":
            BoardList[row-1][column-1] = color
            if color == "Black":
                black_dot(column,row)
            else:
                red_dot(column,row)
            turn_active=False
        else:
            print("Invalid space or space already taken. Please try again.")
    if WinCondition(color):
        print(f"{color} wins!")
        exit()
   
   
def replace_piece(color):
    global turn_count
    turn_active = True
    turn_count += 1
    print("Please select a piece to move:")
    while turn_active:
        row=int(input("Row (1-5):"))
        column=int(input("Column (1-5):"))
        if BoardList[row-1][column-1] == color:
            BoardList[row-1][column-1] = " "
            if color == "Black":
                erase_dot(column,row)
            else:
                erase_dot(column,row)
            turn_active=False
        else:
            print("Invalid choice: That is not your piece. Please try again.")
    turn_active=True
    print("Please select a row and column to move your piece to:")
    while turn_active:
        row=int(input("Row (1-5):"))
        column=int(input("Column (1-5):"))
        if BoardList[row-1][column-1] == " ":
            BoardList[row-1][column-1] = color
            if color == "Black":
                black_dot(column,row)
            else:
                red_dot(column,row)
            turn_active=False
        else:
            print("Invalid space or space already taken. Please try again.")
    if WinCondition(color):
        print(f"{color} wins!")
        exit()




game = True
playerTurn = True
player = "Black"


board_reset()
while (game == True):
    turn_text()
    while (playerTurn == True):
        try:
            user = input()
            if user == "end":
                game = False
                print("Game has ended.")
                break
            elif user == "instructions":
                readInstructions()
            elif user == "move":
                if turn_count<8:
                    place_piece(player)
                else:
                    replace_piece(player)
                break
            elif user == "rules":
                DisplayRules()
            elif user == "illegal": # hypothetical illegal move
                raise(IndexError)
        except IndexError:
            print("Try again!")
        turn_text()


    if player == "Black":
        player = "Red"
    else:
        player = "Black"

