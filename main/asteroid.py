import pygame
from circleshape import *
from main import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        neg_angle = -1*angle
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(neg_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = vector1 * 1.2
        newer_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        newer_asteroid.velocity = vector2 * 1.2
