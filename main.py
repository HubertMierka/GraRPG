import pygame, sys
from settings import *
from level import Level
from player import Player
from difficulty import Difficulty

class Game:

    def __init__(self) -> object:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('19251 Gierka')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.diff = Difficulty()

    def run(self):
        self.screen.fill('black')
        self.diff.display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.level.toggle_menu()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()