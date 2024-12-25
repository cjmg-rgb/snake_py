from settings import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.snake_conf = CONFIG["SNAKE"]
        
        self.image = pygame.Surface((CONFIG["TILE_SIZE"], CONFIG["TILE_SIZE"]))
        self.image.fill(self.snake_conf["SNAKE_HEAD_CLR"])
        self.rect = self.image.get_frect(topleft=pos)
        self.direction = pygame.Vector2(1, 0)
        
        # Last position of the head
        self.last_pos = self.rect.topleft

        # List of the bodies
        self.bodies = []

    def move_bodies(self):
        ### Function to move the bodies in the self.bodies list ###
    
        body_count = len(self.bodies)
        if body_count >= 0:
            for i in range(body_count):
                # Track the current position of the body at ith position
                current_move = self.bodies[i].rect.topleft

                # Move the body at ith position
                if i == 0:
                    self.bodies[i].move(self.last_pos)
                else:                
                    self.bodies[i].move(self.bodies[i-1].last_pos)

                # Set the last position of the body at ith position
                self.bodies[i].last_pos = current_move
        
        # Update the last position which will be used by the first body
        self.last_pos = self.rect.topleft
        
            
    
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
        self.move_bodies()