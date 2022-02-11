
"""
Spyder Editor
This is a temporary script file.
"""

import pygame
import math

surf=pygame.display.set_mode((800,800))
pygame.font.init()
clock=pygame.time.Clock()
run=True
carte=[[[None,8],[None,1],[None,6]],[[None,3],[None,5],[None,7]],[[None,4],[None,9],[None,2]]]
tour=1
pos=None
wincon=None
tit_screen = pygame.image.load("images/BG.png")
start=False




def init_graph(carte):
    surf.fill((0,0,0))
    for x in range (len(carte)):
        for y in range(len(carte[x])):
            if carte[x][y][0]==1:
                pygame.draw.line(surf,(255,0,0),(pygame.display.Info().current_w*x/3,pygame.display.Info().current_h*y/3),(pygame.display.Info().current_w*(x+1)/3,pygame.display.Info().current_h*(y+1)/3))
                pygame.draw.line(surf,(255,0,0),(pygame.display.Info().current_w*x/3,pygame.display.Info().current_h*(y+1)/3),(pygame.display.Info().current_w*(x+1)/3,pygame.display.Info().current_h*y/3))
            if carte[x][y][0]==0:
                pygame.draw.circle(surf,(0,0,255),(math.floor((pygame.display.Info().current_w*x+pygame.display.Info().current_w*(x+1))/6),math.floor((pygame.display.Info().current_h*y+pygame.display.Info().current_h*(y+1))/6)),math.floor(pygame.display.Info().current_h/6),1)
                
    for i in range (2):
        pygame.draw.line(surf,(255,255,255),(0,pygame.display.Info().current_h*(i+1)/3),(pygame.display.Info().current_w,pygame.display.Info().current_h*(i+1)/3))
        pygame.draw.line(surf,(255,255,255),(pygame.display.Info().current_w*(i+1)/3,0),(pygame.display.Info().current_w*(i+1)/3,pygame.display.Info().current_h))
      
        
        
        
def mettre_jour_carte(pos,tour):
    x=int(pos[0]//(pygame.display.Info().current_w/3))
    y=int(pos[1]//(pygame.display.Info().current_h/3))
    if carte[x][y][0] is None:
        carte[x][y][0]=tour%2
        tour+=1
    return carte,tour
    
def wincondef(carte):
    wincon=None
    streak=[[],[]]
    for x in carte:
        for y in x:
            if not y[0] is None:
                streak[y[0]].append(y[1])
                
    for i in range(len(streak)):
        if len(streak[i])>=3:
            for z in range (len(streak[i])):
                if streak[i][len(streak[i])-z-1]+streak[i][len(streak[i])-z-2]+streak[i][len(streak[i])-z-3]==15:
                    wincon=i
    return wincon

def title_screen(tit_screen):
    surf.fill((0,0,0))
    surf.blit(tit_screen,(0,0))
    
            
def win_screen(wincon):
    surf.fill((0,0,0))
    i=['Joueur Bleu','Joueur Rouge']
    myfont = pygame.font.SysFont("Arial", 80)
    letter = myfont.render(i[wincon]+' gagne',0,(255,255,255))
    surf.blit(letter,(100,100))

        

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        if wincon is None:    
            if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0) :
                    pos = pygame.mouse.get_pos() 
                    # print(pos)

    if not start and pos:
        start=True
        pos=None
        init_graph(carte)
        
    elif not start:
        title_screen(tit_screen)
    
    elif pos:
        carte,tour=mettre_jour_carte(pos,tour)
        init_graph(carte)
        wincon=wincondef(carte)
        pos=None
    
    if not wincon is None:
        win_screen(wincon)
    
    pygame.display.flip()


pygame.quit()
