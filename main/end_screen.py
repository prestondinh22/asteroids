import pygame
from main import *
from constants import *
import random
from asteroid import *
from asteroidfield import *

def show_end_screen(score):
    screen = pygame.display.set_mode((1280, 720))  # Adjusted for SCREEN_WIDTH/HEIGHT
    font = pygame.font.Font('PressStart2P-Regular.ttf', 55)
    font2 = pygame.font.Font('PressStart2P-Regular.ttf', 20)

    title_text = font.render("GAME OVER", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(640, 300))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    
    AsteroidField.containers = (asteroidfield, updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield = AsteroidField()
    dt=0
    clock = pygame.time.Clock()
    flicker_timer = 0

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        
        screen.blit(title_text, title_rect)

        updatables.update(dt)

        #
        flicker_timer += 1
        if (flicker_timer // 30) % 2 == 0:  
            
            brightness = random.randint(150, 255)
            flicker_color = (brightness, brightness, brightness)
            start_text = font2.render(f"FINAL SCORE: {score} | Press SPACE to EXIT", True, flicker_color)
            start_rect = start_text.get_rect(center=(630, 600))
            screen.blit(start_text, start_rect)
        
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)  / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            raise SystemExit()
            print('Nice Try')
            