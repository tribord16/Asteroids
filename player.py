from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOT_SPEED,PLAYER_SHOOT_COOLDOWN
from shot import Shot
from pygame import Vector2,draw,key
from pygame import K_a,K_s,K_d,K_w,K_SPACE

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0
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

    def shoot(self):
        if(self.timer > 0): return
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        
        
    ## AFFICHAGE ##
        
    def draw(self, screen):
        draw.polygon(screen,"white",self.triangle(),2)
        

    def update(self, dt):
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotate(-dt)

        if keys[K_d]:
            self.rotate(dt)

        if keys[K_w]:
            self.move(dt)

        if keys[K_s]:
            self.move(-dt)
        
        if keys[K_SPACE]:
            self.shoot()
        
        self.timer -= dt
        