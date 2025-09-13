import pygame
import random
pygame.init()
WIDTH,HEIGHT=800,600
PLAYER_SIZE=50
ENEMY_SIZE=50
NUM_ENEMIES=7
SCORE=0
WHITE=(255,255,255)
GREEN=(0,255,0)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")
player_image=pygame.Surface((PLAYER_SIZE,PLAYER_SIZE))
player_image.fill(GREEN)
enemy_image=pygame.Surface((ENEMY_SIZE,ENEMY_SIZE))
enemy_image.fill((255,0,0))
player_pos=[WIDTH//2,HEIGHT-PLAYER_SIZE-10]
enemies=[[random.randint(0,WIDTH-ENEMY_SIZE),random.randint(0,HEIGHT//2)]for _ in range(NUM_ENEMIES)]
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and player_pos[0]>0:
        player_pos[0]-=5
    if keys[pygame.K_RIGHT]and player_pos[0]<WIDTH-PLAYER_SIZE:
        player_pos[0]+=5
    if keys[pygame.K_UP]and player_pos[1]>0:
        player_pos[1]-=5
    if keys[pygame.K_DOWN]and player_pos[1]<HEIGHT-PLAYER_SIZE:
        player_pos[1]+=5
    player_rect=pygame.Rect(player_pos[0],player_pos[1],PLAYER_SIZE,PLAYER_SIZE)
    for enemy_pos in enemies:
        enemy_rect=pygame.Rect(enemy_pos[0],enemy_pos[1],ENEMY_SIZE,ENEMY_SIZE)
        if player_rect.colliderect(enemy_rect):
            SCORE+=1
            enemy_pos[0]=random.randint(0,WIDTH-ENEMY_SIZE)
            enemy_pos[1]=random.randint(0,HEIGHT//2)
    screen.fill(WHITE)
    screen.blit(player_image,player_pos)
    for enemy_pos in enemies:
        screen.blit(enemy_image,enemy_pos)
    font=pygame.font.Font(None,36)
    score_text=font.render(f'Score:{SCORE}',True,(0,0,0))
    screen.blit(score_text,(10,10))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()