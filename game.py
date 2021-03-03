# Import module  
from tkinter import *
import winsound
  
# Create object  
root = Tk() 
wallImage = PhotoImage(file="best.png")
wallImageHeight = wallImage.height()
wallImageWidth = wallImage.width() 
#____________________________________Variable_________________________________________________________ 
# ENEMY
enemyImage=PhotoImage(file="testenemy.png")

# PLAYER
playerImage=PhotoImage(file="testplayer.png")
#Bullets
canShoot = True
limitBullet=5
#ARRAY2D
array=[
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","E","0","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","w","w","w","0","0","0","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","E","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","w","w","0","0","0","0","0","w"],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","0",'w'],
    ["W","0","0","0","0","0","0","0","0","0","0","0","0","0","E",'w'],
    ["W","P","0","0","0","0","0","0","0","0","0","0","0","w","w",'w'],
    ["w","w","w","W","w","w","W","w","w","W","w","w","w","w","w",'w']
]
positionPlayer = []
screenHeight = wallImageHeight*len(array)
screenWidth = wallImageWidth*len(array[0])
print(screenWidth, screenHeight)

root.geometry = (str(screenHeight)+"x"+str(screenWidth))
# Create Canvas 
canvas = Canvas( root, width =screenWidth, height = screenHeight) 
canvas.pack(fill = "both", expand = True) 

#______________________________________________Move Player______________________________________________________

def playerUp(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]-1][position[0]] == "0":
        array[position[1]-1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    winsound.PlaySound("coin1(1).wav", winsound.SND_FILENAME)
    drawPlayer()

def playerDown(event):
    global array, positionPlayer
    position = []
    for n in range(len(array)):
        for index in  range(len(array[n])):
            if array[n][index]  == "P":
                position.append(index)
                position.append(n)
    if array[position[1]+1][position[0]] == "0":
        array[position[1]+1][position[0]] = "P"
        array[position[1]][position[0]] = "0"
    winsound.PlaySound("coin1(1).wav", winsound.SND_FILENAME)
    drawPlayer()
#_______________________________________________Draw Player_______________________________________   
    
def drawPlayer():
    global positionPlayer
    canvas.delete("player")
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="P":
                positionPlayer = []
                positionPlayer.append(wallImageWidth*col + wallImageWidth/2)
                positionPlayer.append(wallImageHeight*row+wallImageHeight/2)
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = playerImage, tags="player")

def drawGrid():
    global array, wallImage, positionPlayer, positionEnnemies
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    positionEnnemies = [] 
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]=="w" or array[row][col]=="W":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = wallImage)
            if array[row][col]=="E":
                canvas.create_image(wallImageWidth*col + wallImageWidth/2, wallImageHeight*row+wallImageHeight/2, image = enemyImage)
                positionEnnemies.append([row,col])
                
    drawPlayer()

#____________________________________________Function START GAME_________________________________________

def remove(event):
    canvas.delete("remove")
    canvas.delete("delete")
    canvas.move("welcome", 0, 100)


def startGame(event):
    canvas.delete("all")
    winsound.PlaySound("funkyrobot.mp3", winsound.SND_FILENAME)
    drawGrid()

def help(event):
    canvas.move("welcome", 0, -100)
    canvas.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas.create_text(330, 140, text="Following this instruction :",anchor=W, font="Purisa  10",tags="delete")
    canvas.create_text(330, 200, text="1. Press Up Button for move player up",anchor=W, font="Purisa 10",tags="delete")
    canvas.create_text(330, 250, text="2. Press Down Button for move player down",anchor=W, font="Purisa 10",tags="delete")
    canvas.create_text(330, 300, text="3. Press s for shoot the enemy",anchor=W, font="Purisa 10",tags="delete")
    canvas.create_text(330, 350, text="4. You have 5 bullets for shoot the enemies ",anchor=W, font="Purisa 10",tags="delete")
    canvas.create_text(330, 400, text="and kill them for WIN the game otherwize you LOSE" ,anchor=W, font="Purisa 10",tags="delete")


       

def createCircle(event):
    global circle, canShoot,limitBullet, positionEnnemies, ennemyToKill
    ennemyToKill = -1
    gridPositionEnnemy = []
    if canShoot:
        for i in range(len(positionEnnemies)):
            y_ennemy = wallImageHeight*positionEnnemies[i][0]+wallImageHeight/2
            if positionPlayer[1] == y_ennemy:
                ennemyToKill = i
                gridPositionEnnemy = positionEnnemies[i]
        if limitBullet!=0:
            limitBullet-=1
            x_player = positionPlayer[0]
            y_player = positionPlayer[1]
            size = 25
            circle = canvas.create_oval(x_player, y_player, x_player+size, y_player+size, fill = "black")
            moveCircle()
            canShoot = False
    winsound.PlaySound("fall4.wav", winsound.SND_FILENAME)



def moveCircle():
    global circle, canShoot, ennemyToKill, positionEnnemies
    print(ennemyToKill)
    x_bullet = canvas.coords(circle)[0]
  # if x_bullet < SCREEN_WIDTH and if not impactBulletEnemy() and if noHitWall():
    x_ennemy = wallImageWidth* positionEnnemies[ennemyToKill][1] + wallImageWidth/2
    if (ennemyToKill != -1 and x_bullet >= x_ennemy-40):
        canvas.delete(circle)
        canShoot = True
    #    positionEnnemies[row,col]
        # grid[position of your ennemy] = "0"
        # drawGrid()
    elif x_bullet>screenWidth:
        canvas.delete(circle)
        canShoot = True
    else:
        canvas.move(circle, 10, 0)
        canvas.after(100, lambda:moveCircle())

# def impactBulletEnemy()

# Add image file 
bg = PhotoImage(file = "bg.png")

# Display image 
canvas.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 
canvas.create_text(500, 150, text = "Start game!!!", fill="white", font="Times 35 italic bold", tags="welcome")

#Button START
canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas.tag_bind("start", "<Button-1>", startGame)

#Button QUIT
canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas.create_text(515, 450, text = "Help", fill="black", font="Times 35 italic bold", tags="quit")
canvas.tag_bind("quit", "<Button-1>", help)
canvas.tag_bind("remove", "<Button-1>", remove)

#BUTTON FOR MOVE PLAYER

root.bind("<Up>", playerUp)
root.bind("<Down>", playerDown)
root.bind("s",createCircle)



# Display root 
root.mainloop()
