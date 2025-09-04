"""Sprite collision
Outline:
Write a program where a player controls a sprite when two sprites collide , 
the game displaying a win message upon meeting a specific condition."""

import pygame
import random
# Constants for easier adjustments
Screen_width,Screen_height=500,400
Movement_speed=5
Font_size=72
# Initialize Pygame
pygame.init()
# Load and transform the background image
background_image=pygame.transform.scale(pygame.image.load("C:/Users/user/Desktop/Python classes/randome codes i made for fun/background.png"),
                                        (Screen_width,Screen_height))
# Load font once at the beginning
font=pygame.font.SysFont("Times New Roman",Font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color('blue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(
            min(self.rect.x + x_change,Screen_width-self.rect.width),0)
        self.rect.y=max(
            min(self.rect.y + y_change,Screen_height-self.rect.height),0)
# Setup
screen=pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.Group()
# Create sprites
sprite1=Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0, Screen_width - sprite1.rect.width), random.randint(
        0, Screen_height - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2=Sprite(pygame.Color('red'), 20, 30)
sprite1.rect.x,sprite2.rect.y=random.randint(
    0, Screen_width - sprite2.rect.width), random.randint(
        0, Screen_height - sprite2.rect.height)
all_sprites.add(sprite2)

# Game loop control variables
running,won=True,False
clock=pygame.time.Clock()
#main game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                     and event.key == pygame.K_x):
      running = False

  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Movement_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Movement_speed
    sprite1.move(x_change, y_change)

    if sprite1.rect.colliderect(sprite2.rect):
      all_sprites.remove(sprite2)
      won = True

  # Drawing
  screen.blit(background_image, (0, 0))
  all_sprites.draw(screen)

  # Display win message
  if won:
    win_text = font.render("You win!", True, pygame.Color('black'))
    screen.blit(win_text, ((Screen_width - win_text.get_width()) // 2,
                           (Screen_height - win_text.get_height()) // 2))

  pygame.display.flip()
  clock.tick(90)
pygame.quit()