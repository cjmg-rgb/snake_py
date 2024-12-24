from settings import *
from snake import Snake

class Game:
    def __init__(self):
        pygame.init()

        self.WIN = pygame.display.set_mode((CONFIG["WIDTH"], CONFIG["HEIGHT"]))
        self.running = True

        # Sprites
        self.all_sprites = pygame.sprite.Group()

        # Snake
        snake_init_x = (CONFIG["WIDTH"] / 2) - 25
        snake_init_y = (CONFIG["HEIGHT"] / 2) - 25
        self.snake = Snake((snake_init_x, snake_init_y), self.all_sprites)

        self.loop()

    def loop(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(CONFIG["FPS"])
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Updates
            self.all_sprites.update()
            pygame.display.update()

            # Draws
            self.WIN.fill(CONFIG["BG_COLOR"])
            self.all_sprites.draw(self.WIN)

        pygame.quit()