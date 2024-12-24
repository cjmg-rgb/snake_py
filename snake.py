from settings import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.snake_conf = CONFIG["SNAKE"]
        
        self.image = pygame.Surface((CONFIG["TILE_SIZE"], CONFIG["TILE_SIZE"]))
        self.image.fill(self.snake_conf["SNAKE_HEAD_CLR"])
        self.rect = self.image.get_frect(topleft=pos)
        self.direction = pygame.Vector2(1, 0)

    
    def move(self):
        self.rect.left += self.direction.x * 25
        self.rect.top += self.direction.y * 25

        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_d] and self.direction.x != -1:
            self.direction = pygame.Vector2(1, 0)
        if keys[pygame.K_a] and self.direction.x != 1:
            self.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_w] and self.direction.y != 1:
            self.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_s] and self.direction.y != -1:
            self.direction = pygame.Vector2(0, 1)
        


    def update(self):
        self.move()        