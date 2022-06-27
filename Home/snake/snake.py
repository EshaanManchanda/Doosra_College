import os
import random

import pygame

pygame.mixer.init()
pygame.init()

white=(225,225,225)
red=(255,0,0)
black=(0,0,0)
screen_width=1000
screen_height=500

gamewindow= pygame.display.set_mode((screen_width,screen_height))
#Background Image
bgimg = pygame.image.load("gamebk.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
wel= pygame.image.load("welcome.jpeg")
wel= pygame.transform.scale(wel, (screen_width, screen_height)).convert_alpha()
gover= pygame.image.load("game_over.jpg")
gover= pygame.transform.scale(gover, (screen_width, screen_height)).convert_alpha()
pygame.display.set_caption("Snakegame with Eshaan")
pygame.display.update()
clock=pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
done=False

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, s_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, s_size, s_size])
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((233,210,229))
        gamewindow.blit(wel, (0, 0))
        text_screen("Welcome to Snakes", red, 260, 250)
        text_screen("Press Space Bar To Play", red, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bk.mp3')
                    pygame.mixer.music.play()
                    gameprocess()
            pygame.display.update()
        clock.tick(60)
def gameprocess():
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    exit_game = False
    game_over = False
    s_x = 40
    s_y = 55
    s_size = 20
    fps = 35
    vel = 4
    vel_x = 0
    score = 0
    vel_y = 0
    f_size = 15
    food_x = random.randint(30, screen_width/2 )
    food_y = random.randint(30, screen_height/2)
    snk_list = []
    snk_length = 1
    #game loop
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            gamewindow.blit(gover, (0, 0))
            text_screen("Press Enter To Continue",red, 250, 340)
            text_screen("Hiegh Score : "+str(hiscore), red, 350, 390)
            for event in pygame.event.get():
               if event.type== pygame.QUIT:
                   exit_game =True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       welcome()
        else:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                   exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = vel
                        vel_y = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        vel_y = vel
                        vel_x = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = -vel
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        vel_x = -vel
                        vel_y = 0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        score+=20
                        snk_length += 10
            s_x = s_x + vel_x
            s_y = s_y + vel_y
            if abs(s_x-food_x)<20 and abs(s_y-food_y)<20:
                score+=10

                food_x = random.randint(30, screen_width/2)
                food_y = random.randint(30, screen_height/2)
                snk_length += 5
                if score>int(hiscore):
                    hiscore=score
                    # pygame.mixer.music.load('beep.mp3')
                    # pygame.mixer.music.play()
            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score :" +str(score) + "   Hiegh Score:"+str(hiscore),red,5,5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y,f_size,f_size])

            head = []
            head.append(s_x)
            head.append(s_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('ex.mp3')
                pygame.mixer.music.play()
                gamewindow.blit(gover, (0, 0))
            if s_x < 0 or s_x > screen_width or s_y < 0 or s_y > screen_height:
                game_over = True
                pygame.mixer.music.load('ex.mp3')
                pygame.mixer.music.play()
                gamewindow.blit(gover, (0, 0))
            pygame.draw.rect(gamewindow,black,[s_x,s_y,s_size,s_size])
            plot_snake(gamewindow, black, snk_list, s_size)
        pygame.display.update()
        clock.tick(fps)

        pygame.display.update()
    pygame.quit()
    quit()
welcome()