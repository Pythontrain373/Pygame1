import math
import pygame
import random
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.__init__()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/background1.png')
pygame.display.set_caption('Space Invader')
icon=pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/ufo.png')
pygame.display.set_icon(icon)
player_Img=pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/player.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0
enemy_Img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemy_Img.append(pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletImg=pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/bullet.png')
bulletX=0
bulletY=PLAYER_START_Y
bulletX_change=0
bulletY_change=BULLET_SPEED_Y
bullet_state='ready'
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(player_Img, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemy_Img[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE