import pygame
from circleshape import *
from main import *

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        player_rotate_speed = PLAYER_TURN_SPEED * dt
        self.rotation += player_rotate_speed
        return self.rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate((-dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.backward(dt)
        if keys[pygame.K_w]:
            self.forward(dt)
    
    def forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += -forward * PLAYER_SPEED * dt
