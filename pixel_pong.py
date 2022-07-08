import sys, pygame
from sys import exit
import pygame.gfxdraw


class inicio():

    def __init__(self):
        self.pos_x=0
        self.pos_y=250

        self.cambio_vertical=True
        self.cambio_horizontal=True

        self.vertical=0
        self.horizontal=0
        self.arranque()
        

    def arranque(self):
        pygame.init()
        pygame.display.set_caption("PIXEL PONG")
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1000,500))
        text_font = pygame.font.Font(None,50)

        black = 51, 255, 153
        clr = 255,255,255

        keyborad_W = 0
        keyborad_S = 0
        keyborad_UP = 0
        keyborad_DOWN = 0

        pocicion_x_jugador2=980
        pocicion_y_jugador2=175


        pocicion_x_jugador1=10
        pocicion_y_jugador1=175

        pocicion_x_pelota=475
        pocicion_y_pelota=225
        score_1=0
        score_2=0

        

        while True:
            #!scores
            score_surface_1 = text_font.render(str(score_1),False, "Black" )
            score_rect_1= score_surface_1.get_rect( center= (75,50))
            score_surface_2 = text_font.render(str(score_2),False, "Black" )
            score_rect_2= score_surface_2.get_rect( center= (925,50))
            screen.fill(black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        keyborad_UP -=50
                    if event.key == pygame.K_DOWN:
                        keyborad_DOWN +=50
                    
                    if event.key == pygame.K_w:
                        keyborad_S -=50
                    if event.key == pygame.K_s:
                       keyborad_W +=50
            screen.blit(score_surface_1,score_rect_1)
            screen.blit(score_surface_2,score_rect_2)

            
            
            #!JUGADOR1
            self.figuras(keyborad_S,keyborad_W,screen,clr,pocicion_x_jugador1,pocicion_y_jugador1,10,100,0,0)
            #!JUGADOR2
            self.figuras(keyborad_DOWN,keyborad_UP,screen,clr,pocicion_x_jugador2,pocicion_y_jugador2,10,100,0,0)
            #!PELOTA
            self.figuras(0,0,screen,clr,pocicion_x_pelota,pocicion_y_pelota,25,25,self.horizontal,self.vertical)

            
            #!movimiento vertical
            if self.cambio_vertical == True:
                self.vertical += 6
            else:
                self.vertical -= 6
            if self.pos_y >= 500:
                self.cambio_vertical = False
            elif self.pos_y <= 20:
                self.cambio_vertical = True
            #!movimiento horizontal
            if self.cambio_horizontal == True:
                self.horizontal += 6
            else:
                self.horizontal -= 6
            if self.pos_x >= pocicion_x_jugador2-10 and pocicion_y_jugador2+keyborad_DOWN+keyborad_UP<self.pos_y<pocicion_y_jugador2+keyborad_DOWN+keyborad_UP+100:
                self.cambio_horizontal = False
            elif self.pos_x <= pocicion_x_jugador1+10 and pocicion_y_jugador1+keyborad_S+keyborad_W<self.pos_y<pocicion_y_jugador1+100+keyborad_S+keyborad_W:
                self.cambio_horizontal = True
            #! PUNTO
            if self.pos_x >= 1000:
                score_1 +=1
                self.horizontal=0
                self.vertical=0
            elif self.pos_x <= 0:
                score_2 +=1
                self.horizontal=0
                self.vertical=0
            #! FIN JUEGO
            elif score_2 >= 5:
                score_surface_3 = text_font.render("GANO JUGADOR 2",False, "Black" )
                score_rect_3= score_surface_3.get_rect( center= (500,250))
                screen.blit(score_surface_3,score_rect_3)
                self.horizontal=0
                self.vertical=0

            elif score_1 >=5:
                score_surface_4 = text_font.render("GANO JUGADOR 1",False, "Black" )
                score_rect_4= score_surface_4.get_rect(center= (500,250))
                screen.blit(score_surface_4,score_rect_4)
                self.horizontal=0
                self.vertical=0
            




            

            
            
            pygame.display.flip()
            clock.tick(60)
    



    def figuras(self,abajo,arriba,screen,clr,pocicion_x,pocicion_y,tamaño_x,tamaño_y,movimiento_x,movimiento_y):
        for X in range(0,tamaño_x):
                for Y in range(0+abajo+arriba,tamaño_y+abajo+arriba):
                    pygame.gfxdraw.pixel(screen, X+pocicion_x+movimiento_x, Y+pocicion_y+movimiento_y, clr)
                    self.pos_x= X+pocicion_x+movimiento_x
                    self.pos_y= Y+pocicion_y+movimiento_y


            



    

inicio()
