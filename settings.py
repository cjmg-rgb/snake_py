import pygame
import random
from os.path import join


CONFIG = {
    "WIDTH": 800,
    "HEIGHT": 600,
    "TILE_SIZE": 25,
    "BG_COLOR": (50, 50, 50),
    "FPS": 20,
    "SNAKE": {
        "SNAKE_HEAD_CLR": (0, 255, 0),
        "SPEED": 100
    },
    "FRUIT": {
        "CLR": (255, 0, 0),
        "ACTIVE": False
    }
}