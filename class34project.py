import pygame
pygame.init()
WIDTH,HEIGHT=640, 480
WHITE=(255,255,255)
RECT_COLOR=(0,128,255)
FONT_COLOR=(0,0,0)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My first game screen")
rect_width,rect_height=100,50
rect_x=(WIDTH - rect_width) // 2
rect_y=(HEIGHT - rect_height) // 2
font=pygame.font.Font(None, 36)
text=font.render("Hello, Pygame!", True, FONT_COLOR)
text_rect=text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
runnin =True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(WHITE)
    pygame.draw.rect(screen,RECT_COLOR,(rect_x,rect_y,rect_width,rect_height))
    screen.blit(text,text_rect)
    pygame.display.flip()
pygame.quit()

