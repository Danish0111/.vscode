import pygame
import random
import os

pygame.mixer.init()

x = pygame.init()
width = 700
height = 600

snake = pygame.image.load("ws.jpg")
snake = pygame.transform.scale(snake, (width,height))

bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale(bgimg, (width,height))

gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black,[x,y,size,size])

def welcome():
    game_exit = False
    gameWindow.fill(white)
    gameWindow.blit(snake,(0,0))

    text_screen("welcome to snakes",black,50,100)
    text_screen("press q to start",black,50,150)
    # gameWindow.blit(snake,(0,0))
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.mixer.music.load('bm.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(100)
            



def gameloop():

    vel_x = 0
    vel_y = 0

    snake_x = 50
    snake_y = 50

    food_x = random.randint(20,width-100)
    food_y = random.randint(20,height-100)

    game_exit = False
    game_over = False

    size = 20
    fps = 100
    score = 0
    highscore = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
      
   
    while not game_exit:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(hiscore)

            gameWindow.fill((233,233,0))
            
            text_screen("Game over !Press enter to continue",red,10,300)
            text_screen("score : " + str(score),red,270,400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = 2
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x = -2
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_y = - 2
                        vel_x = 0
                    if event.key == pygame.K_DOWN:
                        vel_y = 2
                        vel_x = 0
            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y   
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10 
                pygame.mixer.music.load('eating.mp3')
                pygame.mixer.music.play()

                food_x = random.randint(20,width-100)
                food_y = random.randint(20,height-100)
                snk_length += 3
            if score > int (hiscore):
                hiscore = str(score)

            gameWindow.fill(white)   
            gameWindow.blit(bgimg,(0,0))
            plot_snake(gameWindow,black,snk_list,size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('go.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                pygame.mixer.music.load('go.mp3')
                pygame.mixer.music.play()

            pygame.draw.rect(gameWindow,red,[food_x,food_y,size,size])  
            text_screen("score : "+str(score) + "  High score : " + str(hiscore),red,5,5)      
        pygame.display.update()
        clock.tick(fps) 
    pygame.quit()
    quit()
welcome()