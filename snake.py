import pygame
import random
import os

pygame.mixer.init()


x=pygame.init()

#colours
white=(255, 255, 255)
red=(255, 0, 0)
black=(0, 0, 0)
green=(0, 250, 0)
yellow=(255, 255, 0)
blue=(0, 0 , 255)

#game window
screen_width=850
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

#Background Image
bgimg=pygame.image.load('gameback.jpg')
bgimg=pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snake With Shubho")
pygame.display.update()

#Game specific variables

clock=pygame.time.Clock()

font=pygame.font.SysFont(None, 55)


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    pygame.mixer.music.load('tobu.mp3')
    pygame.mixer.music.play(2)
    while not exit_game:
        gameWindow.fill((200, 230, 200))
        text_screen("THE SNAKE GAME", red, 250, 100)
        text_screen("Welcome Shubhojit",black,240,240)
        text_screen("Enter Space Bar To Play",black,200,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(60)


#Creating Game Loop
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=45
    velocity_x=0
    velocity_y=0
    snake_size=20
    score=0
    init_velocity=3
    food_x=random.randint(20, screen_width/2)
    food_y=random.randint(20, screen_height/2)
    fps=60
    pygame.mixer.music.load('jim.mp3')
    pygame.mixer.music.play(20)
    #Check if hiscore file exits
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")


    with open("hiscore.txt", "r")as f:
        hiscore= f.read()
    

    snk_list=[]
    snk_length=1
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("GAME OVER", red , 320, 200)
            text_screen("You Have Scored :" +str(score), black, 280, 250)
            text_screen("Press Enter To Continue", ((200,0,200)), 230, 300)
            with open("hiscore.txt", "w")as f:
               f.write(str(hiscore))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+=10
                food_x=random.randint(20, screen_width/2)
                food_y=random.randint(20, screen_height/2)
                snk_length+=5

                if score>int(hiscore):
                    hiscore=score


            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score:"+str(score) + " Hiscore: "+str(hiscore),red,5,5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('Game Over.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('Game Over.mp3')
                pygame.mixer.music.play()
            
            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)

        clock.tick(fps)
        pygame.display.update()


    pygame.quit()
    quit()

welcome()
