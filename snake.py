from PIL import Image
import random

end = 100

#setting the snake and the ladders on the board
ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 74, 50: 67, 71: 92, 88: 99}
snake = {32: 10, 34: 6, 48: 26, 62: 18, 88: 89, 95: 56, 97: 78}


#show board function
def show_board():
    img = Image.open('board_image.png')
    img.show()


#check if the point is ladder
def check_ladder(point):
    if (point in ladder.keys()):
        print("climb up!!")
        return ladder[point]
    else:
        return point


#check if the point is snake
def check_snake(point):
    if (point in snake.keys()):
        print("ouch! snake bite!!")
        return snake[point]
    else:
        return point


#check if the end is reached
def reached_end(point):
    return (point >= end)


#play function
def play():
    p1_name = input("enter p1 name: ")  # player 1 name
    p2_name = input("enter p2 name: ")  # player 2 name

    #initialising the
    pp1 = 0
    pp2 = 0
    #turn initialise and turn is alternative

    turn = 0
    #infinite loop
    while (1):
        if (turn % 2 == 0):
            #player 1 turn
            print(p1_name, "your turn")
            #as players choice to continue
            c = int(input("press 1 to continue or 0 to exit: "))
            if (c == 0):
                print(p1_name, 'score : ', pp1)
                print(p2_name, 'score : ', pp2)
                print("Quiting the game!")
                break
            dice = random.randint(1, 6)
            print("Dice showed", dice)
            #add points
            pp1 += dice
            #check ladder
            pp1 = check_ladder(pp1)
            #check for snake
            pp1 = check_snake(pp1)
            #check end point
            if pp1 > end:
                pp1 = end
            print(p1_name, 'Your score', pp1)
            if (reached_end(pp1)):
                print(p1_name, "won")
        else:
            #player 2 turn
            print(p2_name, "your turn")
            #as players choice to continue
            c = int(input("press 1 to continue or 0 to exit: "))
            if (c == 0):
                print(p1_name, 'score : ', pp1)
                print(p2_name, 'score : ', pp2)
                print("Quiting the game!")
                break
            dice = random.randint(1, 6)
            print("Dice showed", dice)
            #add points
            pp2 += dice
            #check ladder
            pp2 = check_ladder(pp1)
            #check for snake
            pp2 = check_snake(pp1)
            #check end point
            if pp2 > end:
                pp2 = end
            print(p2_name, 'Your score', pp2)
            if (reached_end(pp2)):
                print(p2_name, "won")
        turn = turn + 1


#main program
show_board()
play()
