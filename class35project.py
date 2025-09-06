import pygame
pygame.init()
width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Sprite Movement")
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
sprite1=pygame.Rect(100,100,50,50)
sprite2=pygame.Rect(300,300,50,50)
speed=5
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed
    screen.fill(white)
    pygame.draw.rect(screen,red,sprite1)
    pygame.draw.rect(screen,blue,sprite2)
    pygame.display.flip()
pygame.quit()