import pygame
from main import *
from constants import *

def show_start_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont(None, 55)
    title_text = font.render("ASTEROIDS", True, (255, 255, 255))
    start_text = font.render("Press any key to start", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(title_text, title_text.get_rect(center=(640, 250)))
    screen.blit(start_text, title_text.get_rect(center=(560, 300)))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False