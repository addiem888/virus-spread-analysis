import pygame
import sys
import random
from virus import VirusNode
from doctor import Doctor
from pygame.locals import *

pygame.init()
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (185, 195, 255)
bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()

bac_num = 5
doc_num = 1
split_time = 500
done = False
split_times = 18
font = pygame.font.SysFont(None, 80)

def process_events():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            sys.exit()

def init():
    for i in range(bac_num):
        bacteria.add(VirusNode((random.randint(50, width - 50), random.randint(50, height - 50)), split_time))
    for i in range(doc_num):
        doctors.add(Doctor((random.randint(50, width - 50), random.randint(50, height - 50))))

def main():
    init()
    while not done:
        clock.tick(60)
        process_events()
        if len(bacteria) > bac_num * split_times:
            text = font.render("Oh no! You were overrun.", True, (255, 255, 245))
            text_rect = text.get_rect()
        elif len(bacteria) == 0:
            text = font.render("Outbreak stopped!", True, (245, 200, 100))
            text_rect = text.get_rect()
        else:
            doctors.update()
            bacteria.update()
            pygame.sprite.groupcollide(doctors, bacteria, False, True)
            text = font.render("Bacteria Count: {}".format(len(bacteria)), True, (10, 10, 10))
            text_rect = text.get_rect()

        doctors.update()
        bacteria.update()
        screen.fill(color)
        doctors.draw(screen)
        bacteria.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()





if __name__ == "__main__":
    main()
