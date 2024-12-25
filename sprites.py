from settings import *

class Body(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((CONFIG["TILE_SIZE"], CONFIG["TILE_SIZE"]))
        self.image.fill(CONFIG["SNAKE"]["SNAKE_BODY_CLR"])
        self.rect = self.image.get_frect(topleft=pos)
        self.last_pos = None

    def move(self, pos):
        ### Function to move the body ####
        ### pos: the last position of the last body ###
        
        self.rect.topleft = pos                 # Moves the body to the pos (the last position of the previous body)
        self.last_pos = self.rect.topleft       # Sets the last position of this body, for the next body to use

class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((CONFIG["TILE_SIZE"], CONFIG["TILE_SIZE"]))
        self.image.fill(CONFIG["FRUIT"]["CLR"])
        self.rect = self.image.get_frect(topleft=pos)
