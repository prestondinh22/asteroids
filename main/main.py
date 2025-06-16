import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from random import *
from start_screen import *
from end_screen import *
def main():

    pygame.init()
    pygame.display.set_caption("Asteroids")
    show_start_screen()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)
    

    

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (asteroidfield, updatables)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    dt = 0
    global score 
    score = 0
    

    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        for obj in asteroids:
            if obj.collision(player) == True:
                show_end_screen(score)
            
        
        

        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot) == True:
                    shot.kill()
                    if obj.split()==0:
                        score +=1
                    
                

        screen.fill("black")
        
        font = pygame.font.Font('PressStart2P-Regular.ttf', 20)
        title_text = font.render(f"SCORE = {score}", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(115, 50))
        screen.blit(title_text, title_rect)
        
        for obj in drawables:
            obj.draw(screen)

       
        
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()