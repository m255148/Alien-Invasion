import pygame
import sys
#from HW_Ship import Ship
class BlueSky:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
    def run_game(self):
        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            print(event)
if __name__ == '__main__':
    BS = BlueSky()
    BS.run_game()