import pygame, sys
from pygame.locals import *
import timeit
import random


FPS = 200

WINDOWWIDTH = 500
WINDOWHEIGHT = 300
LINETHICKNESS = 10

BLACK = (0,0,0)
WHITE = (255,255,255)

####Menu
def menu():
    pygame.init()
    global DISPLAYSURF

    global BASICFONT1,BASICFONT2
    BASICFONT1 = pygame.font.SysFont('Trebuchet MS', 52)
    BASICFONT2 = pygame.font.SysFont('Trebuchet MS', 25)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("drop")

    Pbox = pygame.Rect(WINDOWWIDTH//2-40,150,75,35)
    Qbox = pygame.Rect(WINDOWWIDTH//2-40,200,75,35)

    ballList = []

    pygame.mouse.set_visible(1)
    
    drawArena()
    drawMenu()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

   
        drawArena()
        ballList = balls(ballList)
        ballList = drawMball(ballList)
        drawBox(Pbox)
        drawBox(Qbox)
        drawMenu()

        mouseP = pygame.mouse.get_pressed()[0]
        mousex,mousey =pygame.mouse.get_pos()
        if mouseP == 1 and mousex >= Pbox.x and mousex <= Pbox.x  +75 and mousey >= Pbox.y and mousey <= Pbox.y +35:
            return False
        elif mouseP == 1 and mousex >= Qbox.x and mousex <= Qbox.x + 75 and mousey >= Qbox.y and mousey <= Qbox.y + 35:
            return True
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawMenu():
    resultSurf1 = BASICFONT1.render("DROP",True,BLACK)
    resultRect1 = resultSurf1.get_rect()
    resultRect1.topleft =  (WINDOWWIDTH//2-60,50)
    DISPLAYSURF.blit(resultSurf1, resultRect1)
    resultSurf2 = BASICFONT2.render("PLAY",True,WHITE)
    resultRect2 = resultSurf2.get_rect()
    resultRect2.topleft = (WINDOWWIDTH//2-30, 150)
    DISPLAYSURF.blit(resultSurf2, resultRect2)
    resultSurf3 = BASICFONT2.render("QUIT",True,WHITE)
    resultRect3 = resultSurf3.get_rect()
    resultRect3.topleft = (WINDOWWIDTH//2-30, 200)
    DISPLAYSURF.blit(resultSurf3, resultRect3)

def balls(ballList):
    if ballList == []: 
        i=0
        xSpawn = random.randint(0,WINDOWWIDTH)
        while(i < 16):
            ySpawn = i * -10
            ball = pygame.Rect(xSpawn,ySpawn,LINETHICKNESS,LINETHICKNESS)
            ballList.append(ball)
            i+=1
    return ballList

def drawMball(ballList):
    c = 0
    for ball in ballList:
        pygame.draw.rect(DISPLAYSURF,(c,c,c),ball)
        ball.y +=6
        c += 17
    if ballList[-1].y > WINDOWWIDTH:
        ballList = []
    return ballList
    
####Menu

####Game
def drawBox(box):
    pygame.draw.rect(DISPLAYSURF,BLACK,box)
    

def drawArena():
    DISPLAYSURF.fill((WHITE))

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF,BLACK,ball)
    if ball.bottom >= WINDOWHEIGHT:
        ball.bottom = WINDOWHEIGHT
    

def drawPlat(plat,ball):
    if ball.top < plat.top and ball.bottom > plat.top and ball.right > plat.left and ball.left < plat.right:
        ball.bottom = plat.top
    if ball.bottom > plat.bottom and ball.top < plat.bottom and ball.right > plat.left and ball.left < plat.right:
        ball.top = plat.bottom
    if ball.bottom > plat.top and ball.top < plat.bottom and ball.left < plat.right and ball.right > plat.right:
        ball.left = plat.right
    if ball.bottom > plat.top and ball.top < plat.bottom and ball.right > plat.left and ball.left< plat.left:
        ball.right = plat.left
    pygame.draw.rect(DISPLAYSURF,BLACK,plat)

def platListCreateUp(platListUp,LINETHICKNESS,WINDOWWIDTH,WINDOWHEIGHT,start):   
    gapx = random.randint(0,WINDOWWIDTH- 60)
    plat1 = pygame.Rect(0, WINDOWHEIGHT,  gapx, LINETHICKNESS)
    
    roll = random.randint(1,3)
    if(roll == 3):
        gapx2 = random.randint(gapx, WINDOWWIDTH -60)
        plat3 = pygame.Rect(gapx2 + 120 , WINDOWHEIGHT  , (WINDOWWIDTH - (gapx2+ 60)), LINETHICKNESS)
        plat2 = pygame.Rect(gapx+60, WINDOWHEIGHT , (gapx2 - gapx),LINETHICKNESS)
        plat = (plat1,plat2,plat3)
    else:
        plat2 = pygame.Rect(gapx+120, WINDOWHEIGHT , (WINDOWWIDTH -(gapx+120)),LINETHICKNESS)
        plat = (plat1, plat2)

    stop = timeit.default_timer()
    gapy = int((stop - start)*2)
    if gapy > 250:
        gapy = 250

    if platListUp == []:
        platListUp.append(plat)
    elif platListUp[-1][1].y < gapy:
        platListUp.append(plat)


    return platListUp

def platListCreateLeft(platListLeft,LINETHICKNESS,WINDOWWIDTH,WINDOWHEIGHT,start):
    flip = random.randint(1,2)
    if flip == 1:
        xSpawn = -10
    else:
        xSpawn = WINDOWWIDTH+10
    
    gapy = random.randint(0,WINDOWHEIGHT-60)
    plat1 = pygame.Rect(xSpawn, 0,LINETHICKNESS,gapy)
    
    roll = random.randint(1,3)
    if(roll == 3):
        gapy2 = random.randint( gapy,WINDOWHEIGHT -60)
        plat3 = pygame.Rect(xSpawn,  gapy2 + 120, LINETHICKNESS,(WINDOWHEIGHT - (gapy2-60)))
        plat2 = pygame.Rect(xSpawn,gapy+60, LINETHICKNESS,(gapy2 - gapy))
        plat = (plat1,plat2,plat3,flip)
    else:
        plat2 = pygame.Rect(xSpawn,gapy+120, LINETHICKNESS,(WINDOWWIDTH +(gapy-120)))
        plat = (plat1, plat2,flip)

        
    
    if platListLeft == []:
        platListLeft.append(plat)
    elif platListLeft[-1][1].x < -30 and flip == 2:
        platListLeft.append(plat)
    elif platListLeft[-1][1].x > WINDOWWIDTH +30 and flip == 1:
        platListLeft.append(plat)


    return platListLeft

def scoreDisplay(start):
    stop = timeit.default_timer()
    score = int(stop - start)
    resultSurf1 = BASICFONT1.render(str(score),True,BLACK)
    resultRect1 = resultSurf1.get_rect()
    resultRect1.topleft =  (WINDOWWIDTH//2,24)
    DISPLAYSURF.blit(resultSurf1, resultRect1)
    return score

def deathCheck(ball,death):
    if ball.bottom < 0:
        death = True
    return death
    
def main():
    pygame.init()
    global DISPLAYSURF

    global BASICFONT1
    BASICFONT1 = pygame.font.SysFont('Trebuchet MS', 36)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("drop")

    ballX = WINDOWWIDTH//2 - LINETHICKNESS //2
    ballY = WINDOWHEIGHT// 2 - LINETHICKNESS//2

    platListUp = []
    platListLeft = []

    ball = pygame.Rect(ballX,ballY,LINETHICKNESS,LINETHICKNESS)
    
    drawArena()
    drawBall(ball)

    start = timeit.default_timer()
    
    pygame.mouse.set_visible(0)

    mousex, mousey = ballX,ballY

    death = False
    
    while death == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.key.name(event.key)

        if pygame.mouse.get_focused() == True:
            mousex, mousey = pygame.mouse.get_pos()

        if ball.centery > mousey:
            ball.y -=3
        if ball.centery < mousey:
            ball.y +=3
        if ball.centerx > mousex:
            ball.x -=3
        if ball.centerx < mousex:
            ball.x +=3
            
                    


        platListUp = platListCreateUp(platListUp,LINETHICKNESS,WINDOWWIDTH,WINDOWHEIGHT,start)
        platListLeft = platListCreateLeft(platListLeft,LINETHICKNESS,WINDOWWIDTH,WINDOWHEIGHT,start)  
                
        drawArena()
        drawBall(ball)

        score = scoreDisplay(start)

        for row in platListUp:

            for plat in row:
                drawPlat(plat,ball)

                plat.y -= 1
        
            if row[0].y < -10:
                del platListUp[0]

        for row in platListLeft:

            for plat in row:
                if type(plat) != int:
                    drawPlat(plat,ball)

                    if row[-1] == 2:
                        plat.x -= 1
                    elif row[-1] == 1:
                        plat.x += 1
            
            if row[-1] == 2 and row[0].x < -30:
                del platListLeft[0]
            elif row[-1] == 1 and row[0].x > WINDOWWIDTH + 30:
                del platListLeft[0]


        death = deathCheck(ball,death)
                
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
    return score

### GAME

### END/HIGHSCORE
def openHigh():
    fin = open("highscore.csv")
    file = fin.read()
    file = file.strip()
    file = file.replace("\n",",")
    file = file.split(",")
    highscore = []
    i = 0
    while(i != 6):
        if i%2 == 0:
            file[i] = int(file[i])
            score = ((file[i]),file[i+1])
            highscore.append(score)
        i+=1
    fin.close()
    highscore.sort(reverse = True)
    return highscore

def newHS(name,score,highscore):
    newScore = (score,name)
    highscore.append(newScore)
    highscore.sort(reverse = True)
    del highscore[-1]
    newHighscore = ""
    fin = open("highscore.csv","w")
    for pair in highscore:
        i = 0
        for unit in pair:
            unit = str(unit)
            if i%2 == 0:
                unit += ","
            else:
                unit += "\n"
            fin.write(unit)
            i += 1
    fin.close()
    return
    
            
def drawName(name,score,highscore):
    # Your name
    resultSurf1 = BASICFONT3.render(name,True,BLACK)
    resultRect1 = resultSurf1.get_rect()
    resultRect1.topright =  (WINDOWWIDTH//2 - 10,225)
    DISPLAYSURF.blit(resultSurf1, resultRect1)
    #Header Gameover
    resultSurf2 = BASICFONT2.render("GAME OVER",True,BLACK)
    resultRect2 = resultSurf2.get_rect()
    resultRect2.center =  (WINDOWWIDTH//2,25)
    DISPLAYSURF.blit(resultSurf2, resultRect2)
    #Header Highscore
    resultSurf3 = BASICFONT1.render("HIGHSCORES",True,BLACK)
    resultRect3 = resultSurf3.get_rect()
    resultRect3.center =  (WINDOWWIDTH//2,75)
    DISPLAYSURF.blit(resultSurf3, resultRect3)
    #YourScore
    resultSurf4 = BASICFONT3.render(str(score),True,BLACK)
    resultRect4 = resultSurf4.get_rect()
    resultRect4.topleft =  (WINDOWWIDTH//2 + 30,225)
    DISPLAYSURF.blit(resultSurf4, resultRect4)
    #NAME/SCORE1
    resultSurf5 = BASICFONT3.render(str(highscore[0][1]),True,BLACK)
    resultRect5 = resultSurf5.get_rect()
    resultRect5.topright =  (WINDOWWIDTH//2 - 10,125)
    DISPLAYSURF.blit(resultSurf5, resultRect5)
    resultSurf6 = BASICFONT3.render(str(highscore[0][0]),True,BLACK)
    resultRect6 = resultSurf6.get_rect()
    resultRect6.topleft =  (WINDOWWIDTH//2 + 30,125)
    DISPLAYSURF.blit(resultSurf6, resultRect6)
    #NAME/SCORE2
    resultSurf7 = BASICFONT3.render(str(highscore[1][1]),True,BLACK)
    resultRect7 = resultSurf7.get_rect()
    resultRect7.topright =  (WINDOWWIDTH//2 - 10,150)
    DISPLAYSURF.blit(resultSurf7, resultRect7)
    resultSurf8 = BASICFONT3.render(str(highscore[1][0]),True,BLACK)
    resultRect8 = resultSurf8.get_rect()
    resultRect8.topleft =  (WINDOWWIDTH//2 + 30,150)
    DISPLAYSURF.blit(resultSurf8, resultRect8)
    #NAME/SCORE3
    resultSurf9 = BASICFONT3.render(str(highscore[2][1]),True,BLACK)
    resultRect9 = resultSurf9.get_rect()
    resultRect9.topright =  (WINDOWWIDTH//2 - 10,175)
    DISPLAYSURF.blit(resultSurf9, resultRect9)
    resultSurf10 = BASICFONT3.render(str(highscore[2][0]),True,BLACK)
    resultRect10 = resultSurf8.get_rect()
    resultRect10.topleft =  (WINDOWWIDTH//2 + 30,175)
    DISPLAYSURF.blit(resultSurf10, resultRect10)
    #INFO
    resultSurf11 = BASICFONT4.render("TYPE DOWN YOUR NAME BELOW AND PRESS MENU OR QUIT",True,BLACK)
    resultRect11 = resultSurf11.get_rect()
    resultRect11.center = (WINDOWWIDTH//2, 216)
    DISPLAYSURF.blit(resultSurf11,resultRect11)
    #BUTTONS
    resultSurf12 = BASICFONT3.render("MENU",True,WHITE)
    resultRect12 = resultSurf12.get_rect()
    resultRect12.topleft = (WINDOWWIDTH//2-80, 260)
    DISPLAYSURF.blit(resultSurf12, resultRect12)
    resultSurf13 = BASICFONT3.render("QUIT",True,WHITE)
    resultRect13 = resultSurf13.get_rect()
    resultRect13.topleft = (WINDOWWIDTH//2+45, 260)
    DISPLAYSURF.blit(resultSurf13, resultRect13)

def end(score):
    pygame.init()
    global DISPLAYSURF

    global BASICFONT1,BASICFONT2,BASICFONT3,BASICFONT4
    BASICFONT1 = pygame.font.SysFont('Trebuchet MS', 36)
    BASICFONT2 = pygame.font.SysFont('Trebuchet MS', 49)
    BASICFONT3 = pygame.font.SysFont('Trebuchet MS', 25)
    BASICFONT4 = pygame.font.SysFont('Trebuchet MS', 16)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("drop")

    highscore = openHigh()

    Qbox = pygame.Rect(WINDOWWIDTH//2+35,260,75,35)
    Mbox = pygame.Rect(WINDOWWIDTH//2-85,260,75,35)

    ballList = []

    pygame.mouse.set_visible(1)
    
    name = ""
    drawArena()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if len(name) < 12:
                    if(event.key == K_a )or(event.key == K_b) or(event.key == K_c )or(event.key == K_d) or(event.key == K_e )or(event.key == K_f )or(event.key == K_g )or(event.key == K_h )or(event.key == K_i )or(event.key == K_j )or(event.key == K_k )or(event.key == K_l )or(event.key == K_m )or(event.key == K_n) or(event.key == K_o )or(event.key == K_p) or(event.key == K_q) or(event.key == K_r) or(event.key == K_s) or(event.key == K_t )or(event.key == K_u )or(event.key == K_v) or(event.key == K_w )or(event.key == K_x )or(event.key == K_y )or(event.key == K_z):
                        name += (pygame.key.name(event.key))
                    elif(event.key == K_SPACE):
                        name += " "
                if event.key == K_BACKSPACE:
                    name= name[0:-1]
                name = name.upper()


        drawArena()
        ballList = balls(ballList)
        ballList = drawMball(ballList)
        drawBox(Mbox)
        drawBox(Qbox)
        drawName(name,score,highscore)

        mouseP = pygame.mouse.get_pressed()[0]
        mousex,mousey =pygame.mouse.get_pos()

        if mouseP == 1 and mousex >= Mbox.x and mousex <= Mbox.x  +75 and mousey >= Mbox.y and mousey <= Mbox.y +35:
            newHS(name,score,highscore)
            return False
        elif mouseP == 1 and mousex >= Qbox.x and mousex <= Qbox.x + 75 and mousey >= Qbox.y and mousey <= Qbox.y + 35:
            newHS(name,score,highscore)
            return True

        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
### END/HIGHSCORE
    
if __name__ == "__main__":
    leave = False
    pygame.mixer.init(44100, -16,2,2048)
    while(leave == False):
        music = random.randint(1,2)
        if music == 1:
            pygame.mixer.music.load("DropMusic1.mp3")
        elif music == 2:
            pygame.mixer.music.load("DropMusic2.mp3")
        pygame.mixer.music.play(-1,0)
        leave = menu()
        if leave == False:
            score = main()
            leave = end(score)
    pygame.quit()
    sys.exit()
    

