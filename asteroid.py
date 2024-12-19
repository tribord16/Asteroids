from circleshape import CircleShape
from pygame import draw
from constants import ASTEROID_MIN_RADIUS

import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS): return
        else:
            randomAngle = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position.x,self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
            asteroid1.velocity = self.velocity.rotate(randomAngle) * 1.2
            asteroid2 = Asteroid(self.position.x,self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
            asteroid2.velocity = self.velocity.rotate(-randomAngle) * 1.2
