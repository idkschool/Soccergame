import pygame 
pygame.init()

Screen_width = 800
Screen_height = 600 


screen= pygame.display.set_mode((Screen_width,Screen_height))

player = pygame.Rect((300,250,50,50))

run = True


while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,0,0),player)


    key= pygame.key.get_pressed()
    if key[pygame.K_a]== True:
        player.move_ip(-1,0)
    if key[pygame.K_d]== True:
        player.move_ip(1,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False  

    pygame.display.update()

pygame.quit()  
