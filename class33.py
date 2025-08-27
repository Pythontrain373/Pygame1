"""Pygame Window
Outline:
Write a Python program to create an empty Pygame window.
# Import Necessary Libraries
import pygame

  
# Initialize required modules
pygame.init()

# Setup window geometry
screen=pygame.display.set_mode((400,500))

# Create a loop to run till the game is quit by the user
done=False
while not done:

	# Clear the event queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


	
	# Make the changes visible
    pygame.display.flip()"""


"""Add Image to the Screen
Outline:
Write a program to create a Pygame window with an image in it. 
Use white colour as background RGB (255, 255, 255). You can use any image of your choice."""
# Initialize Pygame and screen dimensions
import pygame
pygame.init()
Screen_Width,Screen_height=500,500

# Initialize display surface and set title
display_surface=pygame.display.set_mode((Screen_Width,Screen_height))
pygame.display.set_caption('Adding image and background')

# Load and scale images directly
background_image=pygame.transform.scale(
    pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/background.png').convert(),
    (Screen_Width,Screen_height))
penguin_image=pygame.transform.scale(
    pygame.image.load('C:/Users/user/Desktop/Python classes/randome codes i made for fun/Penguin.png').convert_alpha(),(200,200))
penguin_rect=penguin_image.get_rect(center=(Screen_Width// 2,
                                           Screen_height // 2-30))
# Initialize font, render text, and set text position
text=pygame.font.Font(None,36).render('Hello World ',True,
                                         pygame.Color('black'))
text_rect=text.get_rect(center=(Screen_Width//2,Screen_height//2+110))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    game_loop()