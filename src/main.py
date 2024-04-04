import pygame
import sys

from const import * 
from game import Game

class Main:
    
    def __init__(self): #__ :2_
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        
    def mainloop(self):
        
        screen = self.screen
        game = self.game

        
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    pass 
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                # quick application
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update() 
               
                      
main = Main()
main.mainloop()
