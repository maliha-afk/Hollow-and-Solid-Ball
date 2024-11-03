import pygame

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("catch me!")
colour=(250,50,241)
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()



    screen.fill((100,250,250))
    pygame.draw.rect(screen,colour,(150,230,100,100))
    pygame.draw.circle(screen,(240,250,250),(150,150),50)

    pygame.display.flip()