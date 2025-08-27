import pygame
pygame.init()
window_size=(500, 500)
caption="My first game screen"
background_color=(58, 58, 58)
screen=pygame.display.set_mode(window_size)
pygame.display.set_caption(caption)
image=pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/Penguin.png')
image=pygame.transform.scale(image,(300, 300))
image_rect=image.get_rect(center=(window_size[0]//2,window_size[1]//2))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill(background_color)
    screen.blit(image,image_rect)
    pygame.display.flip()
