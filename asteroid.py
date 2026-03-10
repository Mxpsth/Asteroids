from circleshape import CircleShape
from constants import LINE, ASTEROID
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    
    def __init__(self, x, y , radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, LINE.COLOR, self.position, self.radius, LINE.WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID.MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            
            newRoidL = self.copy()
            newRoidL.radius -= ASTEROID.MIN_RADIUS
            newRoidL.velocity *= 1.2
            newRoidL.velocity.rotate_ip(-angle)
            
            newRoidR = newRoidL.copy()
            newRoidR.velocity.rotate_ip(angle*2)

            
    
    def copy(self):
        newObj = Asteroid(self.position.x, self.position.y, self.radius)
        newObj.velocity = self.velocity.copy()
        return newObj