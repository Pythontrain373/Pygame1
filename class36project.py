import pygame
import random
pygame.init()
width,height=800,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Custom Event Example")
WHITE=(255,255,255)
colors=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill(color)
        self.rect=self.image.get_rect(center=(x,y))
    def change_color(self):
        self.image.fill(random.choice(colors))
sprite1=Sprite((255,0,0),200,300)
sprite2=Sprite((0,255,0),600,300)
all_sprites=pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)
CHANGE_COLOR_EVENT=pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT,2000)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()