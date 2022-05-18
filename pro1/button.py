import pygame
pygame.init()
size = [300, 140]
window = pygame.display.set_mode(size)
red = pygame.color.Color('#ff0000')
black = pygame.color.Color('#000000')
white = pygame.color.Color('#ffffff')
colour = red
done = False
while not done:
    window.fill(black)
    pos = pygame.mouse.get_pos()
    if pos[0] >= 20 and pos[0] <= 280 and pos[1] >= 20 and pos[1] <= 120:
        colour = white
    else:
        colour = red
    pygame.draw.rect(window, colour, (20, 20, 260, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if colour == white:
                print ('You pressed the button')
pygame.quit()