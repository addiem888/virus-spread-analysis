import pygame
import random

class Doctor(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("redcross.png")
        self.image = pygame.transform.smoothscale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,5)
        self.speed.rotate_ip(random.randint(0, 360))

    def update(self):
        self.rect.move_ip(self.speed)
        if random.randint(0, 20) == 0:
            rotation = random.choice([-15, 15])
            self.speed.rotate_ip(rotation)
        if self.rect.left < 0 or self.rect.right > 850:
            self.speed[0] *= -1
            self.rect.move_ip(self.speed[0], 0)

        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] *= -1
            self.rect.move_ip(0, self.speed[1])
