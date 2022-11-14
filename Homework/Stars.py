import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Stars:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,600))
        self.bg_color = (230,230,230)
        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        star = Star(self)
        alien_width, alien_height = star.rect.size
        available_space_x = 1200 - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        ship_height = 20
        available_space_y = (1200-(3*alien_height)-ship_height)
        number_rows = available_space_y // (2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_star(alien_number, row_number)

    def _create_star(self, alien_number, row_number):
        star = Star(self)
        alien_width, alien_height = star.rect.size
        star.x = alien_width + 2 * alien_width * alien_number + randint(-20,20)
        star.rect.x = star.x
        star.rect.y = alien_height+2*star.rect.height*row_number + randint(-20,20)
        self.stars.add(star)


class Star(Sprite):
    """A class for a single alien in the fleet"""

    def __init__(self,ai_game):
        """initialize alien starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('STAR.png')
        self.image = pygame.transform.rotozoom(self.image,0, 0.1)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

if __name__ == '__main__':
    BS = Stars()
    BS.run_game()