from settings import *

class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((CONFIG["TILE_SIZE"], CONFIG["TILE_SIZE"]))
        self.image.fill(CONFIG["FRUIT"]["CLR"])
        self.rect = self.image.get_frect(topleft=pos)
