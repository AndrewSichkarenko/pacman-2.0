import pygame
from pac import *
from info import *
pygame.init()


WINDOW_WIDTH = 606
WINDOW_HEIGHT = 606
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load('background2.jpg').convert()
background_image = pygame.transform.scale(background_image, (1072,606))
pygame.display.set_caption("Pacman")
font2 = pygame.font.Font(cfg.FONTPATH, 20)   
text2 = font2.render("The goal of the game: collect all coins.\n Arrow control. Q - teleport forward for a short distance (you can teleport between walls), the player can teleport 3 times in a game. There are 2 teleports on the right and left side of the map that can be used without restrictions. Also, a random number of cherries appear on the field, picking which pacman gets invulnerability to ghosts for a short period of time.", True, BLACK)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(cfg.FONTPATH, 36)
def draw_button():
    button_rect = pygame.Rect(253, 153, 102, 50)
    pygame.draw.rect(window, cfg.SKYBLUE, button_rect)
    text = font.render("PLAY!", True, BLACK)
    window.blit(text, (253,153))
def draw_rect():
    rect = pygame.Rect(15, 348, 576, 200)
    pygame.draw.rect(window, cfg.SKYBLUE, rect)
def handle_button_click():
    main(initialize())
running = True
pygame.mixer.init()
pygame.mixer.music.load(cfg.BGMPATH)
pygame.mixer.music.play(-1, 0.0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(253, 153, 102, 50)
            button_rect2 = pygame.Rect(253, 253, 102, 50)
            if button_rect.collidepoint(mouse_pos):
                handle_button_click()
            elif button_rect2.collidepoint(mouse_pos):
                info()
  
    window.blit(background_image, (0, 0))
    draw_rect()
    window.blit(text2,( 20, 353))
    draw_button()
    
    pygame.display.update()

pygame.quit()