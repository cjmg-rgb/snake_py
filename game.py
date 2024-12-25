from settings import *
from snake import Snake
from sprites import Fruit, Body

class Game:
    def __init__(self):
        pygame.init()

        self.WIN = pygame.display.set_mode((CONFIG["WIDTH"], CONFIG["HEIGHT"]))
        self.running = True

        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.all_fruits = pygame.sprite.Group()

        # Snake
        snake_init_x = (CONFIG["WIDTH"] / 2) - CONFIG["TILE_SIZE"]
        snake_init_y = (CONFIG["HEIGHT"] / 2) - CONFIG["TILE_SIZE"]
        self.snake = Snake((snake_init_x, snake_init_y), self.all_sprites)

        self.loop()

    def collisions(self):
        for fruits in self.all_fruits:
            coll = pygame.sprite.spritecollide(self.snake, self.all_fruits, True)
            if coll:
                body_count = len(self.snake.bodies)
                body_pos = None

                if body_count == 0:
                    body_pos = self.snake.rect.topleft                      # set the position as the head's last position 
                else:
                    body_pos = self.snake.bodies[-1].rect.topleft           # set the position as the last body's last position 

                self.snake.bodies.append(Body(body_pos, self.all_sprites))  # Creates the new body and appends to the list
                CONFIG["FRUIT"]["ACTIVE"] = False

    def spawn_fruit(self):
        if not CONFIG["FRUIT"]["ACTIVE"]:

            x_by_25_list = [x for x in range(CONFIG["WIDTH"]) if x % CONFIG["TILE_SIZE"] == 0]
            y_by_25_list = [y for y in range(CONFIG["HEIGHT"]) if y % CONFIG["TILE_SIZE"] == 0]
            fruit_init_x = random.choice(x_by_25_list)
            fruit_init_y = random.choice(y_by_25_list)

            Fruit((fruit_init_x, fruit_init_y), (self.all_sprites, self.all_fruits))
            CONFIG["FRUIT"]["ACTIVE"] = True

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
            self.collisions()

            # Draws
            self.WIN.fill(CONFIG["BG_COLOR"])
            self.spawn_fruit()
            self.all_sprites.draw(self.WIN)

            pygame.display.update()

        pygame.quit()
