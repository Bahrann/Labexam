import pygame
import sys

def main():

    pygame.init()

    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Canvas with Shapes")
 
    screen.fill((255, 255, 255))
    
 
    pygame.draw.line(screen, (255, 0, 0), (50, 50), (250, 50), 3)
 
    triangle1 = [(250, 100), (200, 200), (300, 200)] 
    triangle2 = [(200, 200), (150, 300), (250, 300)]  
    triangle3 = [(300, 200), (250, 300), (350, 300)]  
    pygame.draw.polygon(screen, (0, 0, 255), triangle1)  
    pygame.draw.polygon(screen, (0, 0, 255), triangle2)  
    pygame.draw.polygon(screen, (0, 0, 255), triangle3)  

    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

if name == "__main__":
    main()