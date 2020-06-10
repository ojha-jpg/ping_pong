import pygame,sys,random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score,opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score +=1
        ball_restart()
    if ball.right >= screen_width:
        opponent_score +=1
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def visuals():
    screen.fill(bg_color)
    pygame.draw.rect(screen,grey,player)
    pygame.draw.rect(screen,grey,opponent)
    pygame.draw.ellipse(screen,grey,ball)
    pygame.draw.aaline(screen,grey,(screen_width/2,0),(screen_width/2,screen_height))

def player_animation():
    player.y +=player_speed

    if player.top<=0 :
        player.top =0
    if player.bottom>=screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top>ball.y :
        opponent.top -= opponent_speed
    if opponent.bottom < ball.y :
        opponent.bottom += opponent_speed

def ball_restart():
    global  ball_speed_y, ball_speed_x
    ball.center=((screen_width/2, screen_height/2))
    ball_speed_y  =random.randint(-5,5)
    ball_speed_x *=random.choice((-1,1))



def show_scores(msg,Color):
    fontstyle=pygame.font.Font("freesansbold.ttf",30)
    mesg= fontstyle.render(msg, True, Color)
    screen.blit (mesg , [screen_width/2-120 , 20])


pygame.init()
clock= pygame.time.Clock()

#main window
screen_width=800
screen_height=400
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PING PONG")


#game rectangles
ball=pygame.Rect(screen_width/2 -15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-20,screen_height/2 -50, 10 , 100 )
opponent=pygame.Rect(10,screen_height/2-50, 10 , 100 )


#color
bg_color =pygame.Color('grey12')
grey =(200,200,200)

ball_speed_y = random.randint(-7,7)
ball_speed_x= 7 * random.choice((1,-1))
player_speed =0
opponent_speed = 20
player_score=0
opponent_score=0

running=True
while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6






    ball_animation()
    player_animation()
    opponent_ai()





    visuals()
    show_scores("CPU :"+ str(opponent_score)+"    "+str(player_score)+ " :PLAYER",(255,6,7))
    pygame.display.flip()
    clock.tick(60)

