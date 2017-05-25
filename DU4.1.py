from turtle import *

#seznam seznamu
def new_game(width, height):
    return [ [ ' ' for i in range(height) ] for i in range(width) ]

#velikost pole
def size(game):
    return (len(game), len(game[0]))

#delka jedne strany ctverce a rychlost zelvy
delka = 30
speed(30000)
cross = False

#namalování pole 
def draw_game(game):
    #clear()
    up()
    width, height = size(game)
    for i in range(width):
        for j in range(height):
            pensize(2)
            goto(delka * i, delka * j)
            down()
            goto(delka * i, delka * (j+1))
            goto(delka * (i+1), delka * (j+1))
            goto(delka * (i+1), delka * j)
            goto(delka * i, delka*j)
            up()
            if (game[i][j] == 1):
                goto(delka * i, delka * j)
                down()
                fillcolor("#B2B2B2")
                begin_fill()
                goto(delka * i, delka * (j+1))
                goto(delka * (i+1), delka * (j+1))
                goto(delka * (i+1), delka * j)
                goto(delka * i, delka * j)
                end_fill()
                up()

#malovani krize a kolecka
def crucifix(x,y):
    global game
    i = x
    j = y
    game[i][j] = 5
    goto(delka * i, delka * j)
    down()
    color("blue")
    pensize(4)
    goto(delka * (i+1), delka * (j+1))
    up()
    goto(delka * i, delka * (j+1))
    down()
    goto(delka * (i+1), delka * j)
    up()
    goto(delka * i, delka * j)
    pensize(2)
    color("black")

def circuit(x,y):
    global game
    i = x
    j = y
    game[i][j] = 4
    goto(delka * (i+0.5), delka * j)
    down()
    color("red")
    pensize(4)
    circle(delka//2)
    up()
    pensize(2)
    color("black")

#start hry s vykreslenim nove hry
def startGame(width, height):
    global game
    game = new_game(width, height)
    draw_game(game)

#funkce na zjiszteni konce gry
def end_game():
    global cross, game
    width, height = size(game)
    for i in range(width):
        for j in range(height):
            if game[i][j] == " ":
                return False
    return True

#hraje hru
def playTurn(x,y):
    global cross, game
    width, height = size(game)
    if (game[x][y] == 1) or (game[x][y] == 4) or (game[x][y] == 5):
        cross = not cross
        return False
    for vx in range(x-1,x+2):
        for vy in range(y-1,y+2):
            if (vx < width and vx >= 0 and vy < height and vy >= 0):
                game[vx][vy] = 1
    if cross:
        crucifix(x,y)
    else:
        circuit(x,y)
    if (end_game() == True):
        print("Konec hry!")
        if cross:
            print("Vyhrál hráč s křížkem")
        else:
            print("Vyhrál hráč s kolečkem")
    cross = not cross
    draw_game(game)

startGame(5, 5)
playTurn(1, 3)
playTurn(4, 4)
playTurn(0, 0)
playTurn(3, 2)
playTurn(3, 0)

