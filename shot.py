from circleshape import CircleShape
from constants import SHOT, LINE
import pygame

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT.RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, LINE.COLOR, self.position, self.radius, LINE.WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
