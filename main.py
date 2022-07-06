import pygame
from player import Player
#from block import Block
#from background import Background

height = 600
width = 600
lineas = 12
puntaje = 0
entidades = []#do these even go here?

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.game_over = False
        self.blocks = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.player = Player()
        self.player.rect.x = width//2
        self.player.rect.y = height//2
        self.sprites.add(self.player)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.vx = -width//lineas
                if event.key == pygame.K_RIGHT:
                    self.player.vx = width//lineas
                if event.key == pygame.K_UP:
                    self.player.vy = -height//lineas
                if event.key == pygame.K_DOWN:
                    self.player.vy = height//lineas
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.vx = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.player.vy = 0
        return True

    def logic(self):
        if not self.game_over:
            self.sprites.update()   

    def display(self, screen):
        screen.fill((0,0,0))
        self.grid(width,height,lineas,screen,(255,255,255))
        if self.game_over:
            font = pygame.font.SysFont("arial",25)
            text = font.render("Game Over, poggers", True, (0,0,0))
            center_x = (width//2) - (text.get_width()//2)
            center_y = (height//2) - (text.get_height()//2)
            screen.blit(text,[center_x, center_y])
        else:
            self.sprites.draw(screen)
        pygame.display.flip()

    def grid(self,width,height,lineas,screen,color):#X just a grid
        wrow = width//lineas
        hrow = height//lineas
        x = 0
        y = 0
        for l in range(lineas):
            x += wrow
            y += hrow
            pygame.draw.line(screen,color,(x,0),(x,width))
            pygame.draw.line(screen,color,(0,y),(width,y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("UnBlock")
    logo = pygame.image.load("Data/GraphicFx/Ball.png").convert_alpha()
    pygame.display.set_icon(logo)
    clock = pygame.time.Clock()
    game = Game(screen)

    open = True
    while open:
        open = game.events()#teclas y situaciones
        game.logic()
        game.display(screen)
        clock.tick(5)
    pygame.quit()

if __name__ == "__main__":
    main()