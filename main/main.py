import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from random import *
from start_screen import *
def main():

    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)
    title_text = font.render("My Game", True, (255, 255, 255))
    start_text = font.render("Press any key to start", True, (255, 255, 255))

    show_start_screen()

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

    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)
        for obj in asteroids:
            if obj.collision(player) == True:
                print('Game Over!')
                raise SystemExit()
        
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot) == True:
                    shot.kill()
                    obj.split()
                    
                
            
        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)

       
        
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()