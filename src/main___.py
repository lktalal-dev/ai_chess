import pygame
import sys

from game import Game
from const import *


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('AI-chess (by TALAL)')
        self.game = Game()
    
    def mainloop(self):

        game = self.game
        screen = self.screen

        while True:
            self.game.show_bg(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            
            pygame.display.update()


main = Main()
main.mainloop()



