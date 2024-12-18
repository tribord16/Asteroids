from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED,PLAYER_SPEED
from pygame import Vector2,draw,key
from pygame import K_a,K_s,K_d,K_w

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 
    ## MOUVEMENTS ##
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    ## AFFICHAGE ##
        
    def draw(self, screen):
        draw.polygon(screen,"white",self.triangle(),2)
        
    

    def update(self, dt):
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotate(dt)

        if keys[K_d]:
            self.rotate(-dt)

        if keys[K_w]:
            self.move(dt)

        if keys[K_s]:
            self.move(-dt)

        