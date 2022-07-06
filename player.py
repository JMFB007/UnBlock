import pygame

class Player(pygame.sprite.Sprite):#objeto jugador
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Data/GraphicFx/Ball.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy