import pygame, sys
from pygame.locals import *
import time

background_colour = (100,100,100)
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.flip()

##Colores
rojo=(195,0,0)
naranja=(195,67,0)
amarillo=(165,165,0)
verde=(0,195,0)
celeste=(21,149,186)
azul=(0,0,195)
morado=(35,0,90)
cafe=(88,24,0)
negro=(20,20,20)
blanco=(255,255,255)
gris=(150,150,150)
##Funcion del menu


def game(cu):
  ###########Codigo Interfaz#########
  (width, height) = (1100, 900)
  screen = pygame.display.set_mode((width, height)) 
  click=False
  pygame.display.set_caption('Juego')
  running = True
  screen.fill((250,250,250))
  pygame.display.flip()
  ##dibuja la cuadricula
  #Cuadros internos
  c=pygame.Rect(100,100,300,300)
  pygame.draw.rect(screen,(150,150,150),c)
  c1=pygame.Rect(500,100,300,300)
  pygame.draw.rect(screen,(150,150,150),c1)
  c2=pygame.Rect(100,500,300,300)
  pygame.draw.rect(screen,(150,150,150),c2)
  c3=pygame.Rect(500,500,300,300)
  pygame.draw.rect(screen,(150,150,150),c3)

  #Seleccion de colores
  co1=pygame.Rect(920,400,50,50)
  pygame.draw.rect(screen,(255,0,0),co1)
  co2=pygame.Rect(980,400,50,50)
  pygame.draw.rect(screen,(255,127,0),co2)
  co3=pygame.Rect(1040,400,50,50)
  pygame.draw.rect(screen,(255,255,0),co3)
  
  co4=pygame.Rect(920,460,50,50)
  pygame.draw.rect(screen,(0,255,0),co4)
  co5=pygame.Rect(980,460,50,50)
  pygame.draw.rect(screen,(81,209,246),co5)
  co6=pygame.Rect(1040,460,50,50)
  pygame.draw.rect(screen,(0,0,255),co6)

  co7=pygame.Rect(920,520,50,50)
  pygame.draw.rect(screen,(75,0,130),co7)
  co8=pygame.Rect(980,520,50,50)
  pygame.draw.rect(screen,(128,64,0),co8)
  co9=pygame.Rect(1040,520,50,50)
  pygame.draw.rect(screen,(20,20,20),co9)

  borrador=pygame.Rect(920,575,120,35)
  pygame.draw.rect(screen,(20,20,20),borrador)
  
  actual=(255,0,0)
  print(cu)
  
  while running:
    mx, my = pygame.mouse.get_pos()
    ##Imagenes
    b=pygame.Rect(920,100,102,42)
    pygame.draw.rect(screen,(255,255,255),b)
    revisar = pygame.image.load('imagenes/revisar.png')
    screen.blit(revisar,(920,100))

    b1=pygame.Rect(920,150,119,39)
    pygame.draw.rect(screen,(255,255,255),b1)
    reiniciar = pygame.image.load('imagenes/reiniciar.png')
    screen.blit(reiniciar,(920,150))

    b2=pygame.Rect(920,200,95,41)
    pygame.draw.rect(screen,(255,255,255),b2)
    nuevo = pygame.image.load('imagenes/nuevo.png')
    screen.blit(nuevo,(915,200))
    
    b3=pygame.Rect(920,250,117,41)
    pygame.draw.rect(screen,(255,255,255),b3)
    guardar = pygame.image.load('imagenes/guardar.png')
    screen.blit(guardar,(920,250))
    
    b4=pygame.Rect(920,300,93,39)
    pygame.draw.rect(screen,(255,255,255),b4)
    cargar = pygame.image.load('imagenes/cargar.png')
    screen.blit(cargar,(920,300))

    b5=pygame.Rect(920,575,93,39)
    pygame.draw.rect(screen,(255,255,255),b5)
    cargar = pygame.image.load('imagenes/borrar.png')
    screen.blit(cargar,(920,575))
    

    
    #Verticales lineas
    #0
    l=pygame.Rect(0,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #1
    l=pygame.Rect(100,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #2
    l=pygame.Rect(200,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #3
    l=pygame.Rect(300,10,10,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #4
    l=pygame.Rect(400,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #5
    l=pygame.Rect(500,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #6
    l=pygame.Rect(600,10,10,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #7
    l=pygame.Rect(700,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #8
    l=pygame.Rect(800,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    #9
    l=pygame.Rect(895,10,5,900)
    pygame.draw.rect(screen,(0,10,0),l)
    
    ##horizontales lineas
    #9
    l=pygame.Rect(0,895,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #8
    l=pygame.Rect(0,800,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #7
    l=pygame.Rect(0,700,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #6
    l=pygame.Rect(0,600,900,10)
    pygame.draw.rect(screen,(0,10,0),l)
    #5
    l=pygame.Rect(0,500,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #4
    l=pygame.Rect(0,400,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #3
    l=pygame.Rect(0,300,900,10)
    pygame.draw.rect(screen,(0,10,0),l)
    #2
    l=pygame.Rect(0,200,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #1
    l=pygame.Rect(0,100,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    #0
    l=pygame.Rect(0,5,900,5)
    pygame.draw.rect(screen,(0,10,0),l)
    
    ##Colores
    rojo=(255,0,0)
    naranja=(255,127,0)
    amarillo=(225,225,0)
    verde=(0,255,0)
    celeste=(81,209,246)
    azul=(0,0,255)
    morado=(75,0,130)
    cafe=(128,64,0)
    negro=(20,20,20)
    blanco=(255,255,255)
    gris=(150,150,150)
    ##Fila 1
    #(1,1)
    cuadrado11=pygame.Rect(5,10,95,90)
    #(1,2)
    cuadrado12=pygame.Rect(105,10,95,90)
    #(1,3)
    cuadrado13=pygame.Rect(205,10,95,90)
    #(1,4)
    cuadrado14=pygame.Rect(310,10,90,90)
    #(1,5)
    cuadrado15=pygame.Rect(405,10,95,90)
    #(1,6)
    cuadrado16=pygame.Rect(505,10,95,90)
    #(1,7)
    cuadrado17=pygame.Rect(610,10,90,90)
    #(1,8)
    cuadrado18=pygame.Rect(705,10,95,90)
    #(1,9)
    cuadrado19=pygame.Rect(805,10,90,90)
    
    ##Fila 2
    #(2,1)
    cuadrado21=pygame.Rect(5,105,95,95)
    #(2,2)
    cuadrado22=pygame.Rect(105,105,95,95)
    #(2,3)
    cuadrado23=pygame.Rect(205,105,95,95)
    #(2,4)
    cuadrado24=pygame.Rect(310,105,90,95)
    #(2,5)
    cuadrado25=pygame.Rect(405,105,95,95)
    #(2,6)
    cuadrado26=pygame.Rect(505,105,95,95)
    #(2,7)
    cuadrado27=pygame.Rect(610,105,90,95)
    #(2,8)
    cuadrado28=pygame.Rect(705,105,95,95)
    #(2,9)
    cuadrado29=pygame.Rect(805,105,90,95)

    ##Fila 3
    #(3,1)
    cuadrado31=pygame.Rect(5,205,95,95)
    #(3,2)
    cuadrado32=pygame.Rect(105,205,95,95)
    #(3,3)
    cuadrado33=pygame.Rect(205,205,95,95)
    #(3,4)
    cuadrado34=pygame.Rect(310,205,90,95)
    #(3,5)
    cuadrado35=pygame.Rect(405,205,95,95)
    #(3,6)
    cuadrado36=pygame.Rect(505,205,95,95)
    #(3,7)
    cuadrado37=pygame.Rect(610,205,90,95)
    #(3,8)
    cuadrado38=pygame.Rect(705,205,95,95)
    #(3,9)
    cuadrado39=pygame.Rect(805,205,90,95)

    ##Fila 4
    #(4,1)
    cuadrado41=pygame.Rect(5,310,95,90)
    #(4,2)
    cuadrado42=pygame.Rect(105,310,95,90)
    #(4,3)
    cuadrado43=pygame.Rect(205,310,95,90)
    #(4,4)
    cuadrado44=pygame.Rect(310,310,90,90)
    #(4,5)
    cuadrado45=pygame.Rect(405,310,95,90)
    #(4,6)
    cuadrado46=pygame.Rect(505,310,95,90)
    #(4,7)
    cuadrado47=pygame.Rect(610,310,90,90)
    #(4,8)
    cuadrado48=pygame.Rect(705,310,95,90)
    #(4,9)
    cuadrado49=pygame.Rect(805,310,90,90)

    ##Fila 5
    #(5,1)
    cuadrado51=pygame.Rect(5,405,95,95)
    #(5,2)
    cuadrado52=pygame.Rect(105,405,95,95)
    #(5,3)
    cuadrado53=pygame.Rect(205,405,95,95)
    #(5,4)
    cuadrado54=pygame.Rect(310,405,90,95)
    #(5,5)
    cuadrado55=pygame.Rect(405,405,95,95)
    #(5,6)
    cuadrado56=pygame.Rect(505,405,95,95)
    #(5,7)
    cuadrado57=pygame.Rect(610,405,90,95)
    #(5,8)
    cuadrado58=pygame.Rect(705,405,95,95)
    #(5,9)
    cuadrado59=pygame.Rect(805,405,90,95)

    ##Fila 6
    #(6,1)
    cuadrado61=pygame.Rect(5,505,95,95)
    #(6,2)
    cuadrado62=pygame.Rect(105,505,95,95)
    #(6,3)
    cuadrado63=pygame.Rect(205,505,95,95)
    #(6,4)
    cuadrado64=pygame.Rect(310,505,90,95)
    #(6,5)
    cuadrado65=pygame.Rect(405,505,95,95)
    #(6,6)
    cuadrado66=pygame.Rect(505,505,95,95)
    #(6,7)
    cuadrado67=pygame.Rect(610,505,90,95)
    #(6,8)
    cuadrado68=pygame.Rect(705,505,95,95)
    #(6,9)
    cuadrado69=pygame.Rect(805,505,90,95)

    ##Fila 7
    #(7,1)
    cuadrado71=pygame.Rect(5,610,95,90)
    #(7,2)
    cuadrado72=pygame.Rect(105,610,95,90)
    #(7,3)
    cuadrado73=pygame.Rect(205,610,95,90)
    #(7,4)
    cuadrado74=pygame.Rect(310,610,90,90)
    #(7,5)
    cuadrado75=pygame.Rect(405,610,95,90)
    #(7,6)
    cuadrado76=pygame.Rect(505,610,95,90)
    #(7,7)
    cuadrado77=pygame.Rect(610,610,90,90)
    #(7,8)
    cuadrado78=pygame.Rect(705,610,95,90)
    #(7,9)
    cuadrado79=pygame.Rect(805,610,90,90)

    ##Fila 8
    #(8,1)
    cuadrado81=pygame.Rect(5,705,95,95)
    #(8,2)
    cuadrado82=pygame.Rect(105,705,95,95)
    #(8,3)
    cuadrado83=pygame.Rect(205,705,95,95)
    #(8,4)
    cuadrado84=pygame.Rect(310,705,90,95)
    #(8,5)
    cuadrado85=pygame.Rect(405,705,95,95)
    #(8,6)
    cuadrado86=pygame.Rect(505,705,95,95)
    #(8,7)
    cuadrado87=pygame.Rect(610,705,90,95)
    #(8,8)
    cuadrado88=pygame.Rect(705,705,95,95)
    #(8,9)
    cuadrado89=pygame.Rect(805,705,90,95)

    ##Fila 9
    #(9,1)
    cuadrado91=pygame.Rect(5,805,95,95)
    #(9,2)
    cuadrado92=pygame.Rect(105,805,95,95)
    #(9,3)
    cuadrado93=pygame.Rect(205,805,95,95)
    #(9,4)
    cuadrado94=pygame.Rect(310,805,90,95)
    #(9,5)
    cuadrado95=pygame.Rect(405,805,95,95)
    #(9,6)
    cuadrado96=pygame.Rect(505,805,95,95)
    #(9,7)
    cuadrado97=pygame.Rect(610,805,90,95)
    #(9,8)
    cuadrado98=pygame.Rect(705,805,95,95)
    #(9,9)
    cuadrado99=pygame.Rect(805,805,90,95)

    ##Marca seleccion de colores
    #1
    e=pygame.Rect(918,398,500,500)
    if co1.collidepoint((mx,my)):
      if click:
        actual=rojo
        co=pygame.Rect(918,398,54,54)
        pygame.draw.rect(screen,(255,255,255),e)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,rojo,co1)
        pygame.draw.rect(screen,naranja,co2)
        pygame.draw.rect(screen,amarillo,co3)
        pygame.draw.rect(screen,verde,co4)
        pygame.draw.rect(screen,celeste,co5)
        pygame.draw.rect(screen,azul,co6)
        pygame.draw.rect(screen,morado,co7)
        pygame.draw.rect(screen,cafe,co8)
        pygame.draw.rect(screen,negro,co9)
    #2
    if co2.collidepoint((mx,my)):
      if click:
        actual=naranja
        co=pygame.Rect(978,398,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,naranja,co2)
    #3
    if co3.collidepoint((mx,my)):
      if click:
        actual=amarillo
        co=pygame.Rect(1038,398,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,amarillo,co3)
    #4  
    if co4.collidepoint((mx,my)):
      if click:
        actual=verde
        co=pygame.Rect(918,458,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,verde,co4)
    #5   
    if co5.collidepoint((mx,my)):
      if click:
        actual=celeste
        co=pygame.Rect(978,458,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,celeste,co5)
    #6 
    if co6.collidepoint((mx,my)):
      if click:
        actual=azul
        co=pygame.Rect(1038,458,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,azul,co6)

    #7 
    if co7.collidepoint((mx,my)):
      if click:
        actual=morado
        co=pygame.Rect(918,518,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,morado,co7)
       
    #8 
    if co8.collidepoint((mx,my)):
      if click:
        actual=cafe
        co=pygame.Rect(978,518,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,cafe,co8)
      

    #9
    if co9.collidepoint((mx,my)):
      if click:
        actual=negro
        co=pygame.Rect(1038,518,54,54)
        pygame.draw.rect(screen,(0,0,0),co)
        pygame.draw.rect(screen,negro,co9)
    #9
    if borrador.collidepoint((mx,my)):
      if click:
        actual=blanco
        co=pygame.Rect(917,572,128,42)
        pygame.draw.rect(screen,(0,0,0),co)
        screen.blit(cargar,(920,575))
        
    
        
    ##Marca casillas
    #1
    ##borrar en gris
    if c.collidepoint((mx,my)) and actual==blanco:
      if click:
        actual=gris
        print('borrador')
    if c1.collidepoint((mx,my)) and actual==blanco:
      if click:
        actual=gris
        print('borrador1')
        
    if c2.collidepoint((mx,my)) and actual==blanco:
      if click:
        actual=gris
        print('borrador2')

    if c3.collidepoint((mx,my)) and actual==blanco:
      if click:
        actual=gris
        print('borrador3')

    elif not c.collidepoint((mx,my)) and actual==gris:
      if click:
        actual=blanco
        
    elif not c1.collidepoint((mx,my)) and actual==gris:
      if click:
        actual=blanco
        
    elif not c2.collidepoint((mx,my)) and actual==gris:
      if click:
        actual=blanco
        
    elif not c3.collidepoint((mx,my)) and actual==gris:
      if click:
        actual=blanco
        

    ##1
    if cuadrado11.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado11)
        sec1.lista[0]=actual
        print(sec1.lista)
        print('1,1')
  
    if cuadrado12.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado12)
        sec1.lista[1]=actual
        print('1,2')
        
    if cuadrado13.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado13)
        sec1.lista[2]=actual
        print('1,3')
        
    if cuadrado14.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado14)
        sec1.lista[3]=actual
        print('1,4')
        
    if cuadrado15.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado15)
        sec1.lista[4]=actual
        print('1,5')
        
    if cuadrado16.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado16)
        sec1.lista[5]=actual
        print('1,6')
        
    if cuadrado17.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado17)
        sec1.lista[6]=actual
        print('1,7')
        
    if cuadrado18.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado18)
        sec1.lista[7]=actual
        print('1,8')
        
    if cuadrado19.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado19)
        sec1.lista[8]=actual
        print('1,9')
        
    ##2
    if cuadrado21.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado21)
        sec2.lista[0]=actual
        print('2,1')
  
    if cuadrado22.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado22)
        sec2.lista[1]=actual
        print('2,2')
        
    if cuadrado23.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado23)
        sec2.lista[2]=actual
        print('2,3')
        
    if cuadrado24.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado24)
        sec2.lista[3]=actual
        print('2,4')
        
    if cuadrado25.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado25)
        sec2.lista[4]=actual
        print('2,5')
        
    if cuadrado26.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado26)
        sec2.lista[5]=actual
        print('2,6')
        
    if cuadrado27.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado27)
        sec2.lista[6]=actual
        print('2,7')
        
    if cuadrado28.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado28)
        sec2.lista[7]=actual
        print('2,8')
        
    if cuadrado29.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado29)
        sec2.lista[8]=actual
        print('2,9')

    ##3
    if cuadrado31.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado31)
        sec3.lista[0]=actual
        print('3,1')
  
    if cuadrado32.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado32)
        sec3.lista[1]=actual
        print('3,2')
        
    if cuadrado33.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado33)
        sec3.lista[2]=actual
        print('3,3')
        
    if cuadrado34.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado34)
        sec3.lista[3]=actual
        print('3,4')
        
    if cuadrado35.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado35)
        sec3.lista[4]=actual
        print('3,5')
        
    if cuadrado36.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado36)
        sec3.lista[5]=actual
        print('3,6')
        
    if cuadrado37.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado37)
        sec3.lista[6]=actual
        print('3,7')
        
    if cuadrado38.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado38)
        sec3.lista[7]=actual
        print('3,8')
        
    if cuadrado39.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado39)
        sec3.lista[8]=actual
        print('3,9')

    ##4
    if cuadrado41.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado41)
        sec4.lista[0]=actual
        print('4,1')
  
    if cuadrado42.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado42)
        sec4.lista[1]=actual
        print('4,2')
        
    if cuadrado43.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado43)
        sec4.lista[2]=actual
        print('4,3')
        
    if cuadrado44.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado44)
        sec4.lista[3]=actual
        print('4,4')
        
    if cuadrado45.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado45)
        sec4.lista[4]=actual
        print('4,5')
        
    if cuadrado46.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado46)
        sec4.lista[5]=actual
        print('4,6')
        
    if cuadrado47.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado47)
        sec4.lista[6]=actual
        print('4,7')
        
    if cuadrado48.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado48)
        sec4.lista[7]=actual
        print('4,8')
        
    if cuadrado49.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado49)
        sec4.lista[8]=actual
        print('4,9')

    ##5
    if cuadrado51.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado51)
        sec5.lista[0]=actual
        print('5,1')
  
    if cuadrado52.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado52)
        sec5.lista[1]=actual
        print('5,2')
        
    if cuadrado53.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado53)
        sec5.lista[2]=actual
        print('5,3')
        
    if cuadrado54.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado54)
        sec5.lista[3]=actual
        print('5,4')
        
    if cuadrado55.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado55)
        sec5.lista[4]=actual
        print('5,5')
        
    if cuadrado56.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado56)
        sec5.lista[5]=actual
        print('5,6')
        
    if cuadrado57.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado57)
        sec5.lista[6]=actual
        print('5,7')
        
    if cuadrado58.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado58)
        sec5.lista[7]=actual
        print('5,8')
        
    if cuadrado59.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado59)
        sec5.lista[8]=actual
        print('5,9')

    ##6
    if cuadrado61.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado61)
        sec6.lista[0]=actual
        print('6,1')
  
    if cuadrado62.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado62)
        sec6.lista[1]=actual
        print('6,2')
        
    if cuadrado63.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado63)
        sec6.lista[2]=actual
        print('6,3')
        
    if cuadrado64.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado64)
        sec6.lista[3]=actual
        print('5,4')
        
    if cuadrado65.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado65)
        sec6.lista[4]=actual
        print('6,5')
        
    if cuadrado66.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado66)
        sec6.lista[5]=actual
        print('6,6')
        
    if cuadrado67.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado67)
        sec6.lista[6]=actual
        print('6,7')
        
    if cuadrado68.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado68)
        sec6.lista[7]=actual
        print('6,8')
        
    if cuadrado69.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado69)
        sec6.lista[8]=actual
        print('6,9')

    ##7
    if cuadrado71.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado71)
        sec7.lista[0]=actual
        print('7,1')
  
    if cuadrado72.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado72)
        sec7.lista[1]=actual
        print('7,2')
        
    if cuadrado73.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado73)
        sec7.lista[2]=actual
        print('7,3')
        
    if cuadrado74.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado74)
        sec7.lista[3]=actual
        print('7,4')
        
    if cuadrado75.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado75)
        sec7.lista[4]=actual
        print('7,5')
        
    if cuadrado76.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado76)
        sec7.lista[5]=actual
        print('7,6')
        
    if cuadrado77.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado77)
        sec7.lista[6]=actual
        print('7,7')
        
    if cuadrado78.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado78)
        sec7.lista[7]=actual
        print('7,8')
        
    if cuadrado79.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado79)
        sec7.lista[8]=actual
        print('7,9')

    ##8
    if cuadrado81.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado81)
        sec8.lista[0]=actual
        print('8,1')
  
    if cuadrado82.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado82)
        sec8.lista[1]=actual
        print('8,2')
        
    if cuadrado83.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado83)
        sec8.lista[2]=actual
        print('8,3')
        
    if cuadrado84.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado84)
        sec8.lista[3]=actual
        print('8,4')
        
    if cuadrado85.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado85)
        sec8.lista[4]=actual
        print('8,5')
        
    if cuadrado86.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado86)
        sec8.lista[5]=actual
        print('8,6')
        
    if cuadrado87.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado87)
        sec8.lista[6]=actual
        print('8,7')
        
    if cuadrado88.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado88)
        sec8.lista[7]=actual
        print('8,8')
        
    if cuadrado89.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado89)
        sec8.lista[8]=actual
        print('8,9')

    ##9
    if cuadrado91.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado91)
        sec9.lista[0]=actual
        print('9,1')
  
    if cuadrado92.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado92)
        sec9.lista[1]=actual
        print('9,2')
        
    if cuadrado93.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado93)
        sec9.lista[2]=actual
        print('9,3')
        
    if cuadrado94.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado94)
        sec9.lista[3]=actual
        print('9,4')
        
    if cuadrado95.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado95)
        sec9.lista[4]=actual
        print('9,5')
        
    if cuadrado96.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado96)
        sec9.lista[5]=actual
        print('9,6')
        
    if cuadrado97.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado97)
        sec9.lista[6]=actual
        print('9,7')
        
    if cuadrado98.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado98)
        sec9.lista[7]=actual
        print('9,8')
        
    if cuadrado99.collidepoint((mx,my)):
      if click:
        pygame.draw.rect(screen,actual,cuadrado99)
        sec9.lista[8]=actual
        print('9,9')
    ##opciones de la derecha
    if b.collidepoint((mx,my)):
      if click:
        print('revisar')
  
    if b1.collidepoint((mx,my)):
      if click:
        print('reiniciar')
        reinicio()
    if b2.collidepoint((mx,my)):
      if click:
        cuad1.lista=[0,0,0,0,0,0,0,0,0]
        cuad2.lista=[0,0,0,0,0,0,0,0,0]
        cuad3.lista=[0,0,0,0,0,0,0,0,0]
        cuad4.lista=[0,0,0,0,0,0,0,0,0]
        cuad5.lista=[0,0,0,0,0,0,0,0,0]
        cuad6.lista=[0,0,0,0,0,0,0,0,0]
        cuad7.lista=[0,0,0,0,0,0,0,0,0]
        cuad8.lista=[0,0,0,0,0,0,0,0,0]
        cuad9.lista=[0,0,0,0,0,0,0,0,0]
        iniciar()
        
        print('nuevo')
    if b3.collidepoint((mx,my)):
      if click:
        guardarr(cu)
        print('guardar')
    if b4.collidepoint((mx,my)):
      if click:
        print('cargar')
        cuad1.lista=[0,0,0,0,0,0,0,0,0]
        cuad2.lista=[0,0,0,0,0,0,0,0,0]
        cuad3.lista=[0,0,0,0,0,0,0,0,0]
        cuad4.lista=[0,0,0,0,0,0,0,0,0]
        cuad5.lista=[0,0,0,0,0,0,0,0,0]
        cuad6.lista=[0,0,0,0,0,0,0,0,0]
        cuad7.lista=[0,0,0,0,0,0,0,0,0]
        cuad8.lista=[0,0,0,0,0,0,0,0,0]
        cuad9.lista=[0,0,0,0,0,0,0,0,0]
        abrir()
        
    click=False
    
    ###Pinta las casillas iniciales
    
    ##Colores
    for i in range(0,9):
      for e in range(0,9):
        if cu[i][e] != 0:
          if i==0:
            if e==0:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado11)
            if e==1:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado12)
            if e==2:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado13)
            if e==3:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado21)
            if e==4:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado22)
            if e==5:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado23)
            if e==6:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado31)
            if e==7:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado32)
            if e==8:
              pygame.draw.rect(screen,cuad1.lista[e],cuadrado33)

          if i==1:
            if e==0:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado14)    
            if e==1:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado15)
            if e==2:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado16)
            if e==3:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado24)
            if e==4:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado25)
            if e==5:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado26)
            if e==6:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado34)
            if e==7:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado35)
            if e==8:
              pygame.draw.rect(screen,cuad2.lista[e],cuadrado36)
              
          if i==2:
            if e==0:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado17)
            if e==1:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado18)
            if e==2:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado19)
            if e==3:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado27)
            if e==4:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado28)
            if e==5:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado29)
            if e==6:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado37)
            if e==7:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado38)
            if e==8:
              pygame.draw.rect(screen,cuad3.lista[e],cuadrado39)
              
          if i==3:
            if e==0:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado41)
            if e==1:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado42)
            if e==2:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado42)
            if e==3:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado51)
            if e==4:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado52)
            if e==5:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado53)
            if e==6:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado61)
            if e==7:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado62)
            if e==8:
              pygame.draw.rect(screen,cuad4.lista[e],cuadrado63)
              
          if i==4:
            if e==0:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado44)
            if e==1:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado45)
            if e==2:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado46)
            if e==3:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado54)
            if e==4:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado55)
            if e==5:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado56)
            if e==6:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado64)
            if e==7:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado65)
            if e==8:
              pygame.draw.rect(screen,cuad5.lista[e],cuadrado66)

          if i==5:
            if e==0:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado47)
            if e==1:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado48)
            if e==2:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado49)
            if e==3:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado57)
            if e==4:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado58)
            if e==5:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado59)
            if e==6:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado67)
            if e==7:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado68)
            if e==8:
              pygame.draw.rect(screen,cuad6.lista[e],cuadrado69)

          if i==6:
            if e==0:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado71)
            if e==1:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado72)
            if e==2:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado73)
            if e==3:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado81)
            if e==4:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado82)
            if e==5:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado83)
            if e==6:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado91)
            if e==7:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado92)
            if e==8:
              pygame.draw.rect(screen,cuad7.lista[e],cuadrado93)

          if i==7:
            if e==0:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado74)
            if e==1:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado75)
            if e==2:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado76)
            if e==3:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado84)
            if e==4:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado85)
            if e==5:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado86)
            if e==6:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado94)
            if e==7:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado95)
            if e==8:
              pygame.draw.rect(screen,cuad8.lista[e],cuadrado96)

          if i==8:
            if e==0:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado77)
            if e==1:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado78)
            if e==2:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado79)
            if e==3:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado87)
            if e==4:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado88)
            if e==5:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado89)
            if e==6:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado97)
            if e==7:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado98)
            if e==8:
              pygame.draw.rect(screen,cuad9.lista[e],cuadrado99)
     
        
    #######codigo logica######
    

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click=True
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          screen.fill((100,100,100))
          pygame.display.flip()
          running=False
          print('salir')
    
    pygame.display.update()


    
from random import randint
from random import sample

class cuadricula:
    def __init__(self):
        self.lista=[0,0,0,0,0,0,0,0,0]
##repetido en cuadrado 3x3 
def repetido(M):
    copia=M
    while copia!=[]:
        lista=copia[0]
        for i in range(0, len(lista)-1):
            for p in range(i+1,len(lista)):
                if lista[i]==0 or lista[p]==0:
                    pass
                elif lista[i]==lista[p]:
                    lista[i]=0
                    
                else:
                    pass
        copia=copia[1:]
    print(M)
    return repetidoM(M)
  
##internos
def repetidoM(M):
    game(M)
##botones izquierda
  
def reinicio():
    c=pygame.Rect(0,0,900,1000)
    pygame.draw.rect(screen,(255,255,255),c)
    c=pygame.Rect(100,100,300,300)
    pygame.draw.rect(screen,(150,150,150),c)
    c1=pygame.Rect(500,100,300,300)
    pygame.draw.rect(screen,(150,150,150),c1)
    c2=pygame.Rect(100,500,300,300)
    pygame.draw.rect(screen,(150,150,150),c2)
    c3=pygame.Rect(500,500,300,300)
    pygame.draw.rect(screen,(150,150,150),c3)
    
def nuevo():
    iniciar()

#Cargar(abrir archivo)

def limpiar(file,lista):
    color=(26,26,200)
    for ele in file:
        lista.append(ele.split(';'))
    lista=lista[0]
    listaF=[]
    for ele in range(0,len(lista)):
        r=lista[ele].split('-')
        listaF=listaF+[r]
    print(lista)
    print('===================')
    print(listaF)
    for ele in range(0,len(listaF)):
        for i in range(0,len(listaF[ele])):
            if listaF[ele][i]== '(195, 0, 0)' or listaF[ele][i]=='(255,0,0)':
                color=rojo
                
            if listaF[ele][i]=='(195,67,0)' or listaF[ele][i]=='(255,127,0)':
       
                color=naranja
            if listaF[ele][i]=='(165,165,0)' or listaF[ele][i]=='(225,225,0)':
                color=amarillo
   
            if listaF[ele][i]=='(0,195,0)' or listaF[ele][i]=='(0,255,0)':
                color=verde
           
            if listaF[ele][i]=='(21,149,186)' or listaF[ele][i]=='(81,209,246)':
                color=celeste
            if listaF[ele][i]=='(0,0,195)' or listaF[ele][i]=='(0,0,255)':
                color=azul
             
            if listaF[ele][i]=='(35,0,90)' or listaF[ele][i]=='(75,0,130)':
                color=morado
               
            if listaF[ele][i]=='(88,24,0)' or listaF[ele][i]=='(128,64,0)':
                color=cafe
            if listaF[ele][i]=='10' or listaF[ele][i]=='(10,10,10)':
                color=negro
                
            elif listaF[ele][i]=='0' or listaF[ele][i]=='[' or listaF[ele][i]==']' or listaF[ele][i]==' ':
                pass
            elif ele==0:
                cuad1.lista.remove(0)
                cuad1.lista.insert(i-1,color)
            elif ele==1:
                cuad2.lista.insert(i-1,color)
                cuad2.lista.remove(0)
            elif ele==2:
                cuad3.lista.remove(0)
                cuad3.lista.insert(i-1,color)
            elif ele==3:
                cuad4.lista.remove(0)
                cuad4.lista.insert(i-1,color)
            elif ele==4:
                cuad5.lista.remove(0)
                cuad5.lista.insert(i-1,color)
            elif ele==5:
                cuad6.lista.remove(0)
                cuad6.lista.insert(i-1,color)
            elif ele==6:
                cuad7.lista.remove(0)
                cuad7.lista.insert(i-1,color)
            elif ele==7:
                cuad8.lista.remove(0)
                cuad8.lista.insert(i-1,color)
            elif ele==8:
                cuad9.lista.remove(0)
                cuad9.lista.insert(i-1,color)
            else:
                pass
                            
            
    print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    print(cuad1.lista)
    print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    cu=[]
    cu=cu+[cuad1.lista]
    cu=cu+[cuad2.lista]
    cu=cu+[cuad3.lista]
    cu=cu+[cuad4.lista]
    cu=cu+[cuad5.lista]
    cu=cu+[cuad6.lista]
    cu=cu+[cuad7.lista]
    cu=cu+[cuad8.lista]
    cu=cu+[cuad9.lista]
    game(cu)
                
                
    
def abrir():
    x=open('texto.txt','r')
    file=[]
    for line in x:
        file.append(line)
    x.close
    lista=[]
    limpiar(file, lista)

#Guardar(guardar la partida)
def guardarr(cu):
    file= open('texto.txt','r+')
    file.truncate(0)
    cu=str(cu)
    f=cu.replace('],','];')
    f=f.replace('(195, 0, 0)','(195,0,0)')
    f=f.replace('(195, 67, 0)','(195,67,0)')
    f=f.replace('(165, 165, 0)','(165,165,0)')
    f=f.replace('(0, 195, 0)','(0,195,0)')
    f=f.replace('(21, 149, 186)','(21,149,186)')
    f=f.replace('(0, 0, 195)','(0,0,195)')
    f=f.replace('(35, 0, 90)','(35,0,90)')
    f=f.replace('(88, 24, 0)','(88,24,0)')
    f=f.replace(', ','-')
    f=f.replace(' ','')
    #f=f[1:len(f)-1]
    file.write(f)
    print('vvvvvvvvvvvvvvvvvvvvvvv')
    print(f)
    print('vvvvvvvvvvvvvvvvvvvvvvv')
    print(cu)
    print('vvvvvvvvvvvvvvvvvvvvvvv')
  
##iniciar
def iniciar():
    rand=randint(15,20)   #numero del 8 al 20  
    rand1=randint(1,9)  #numero del 1 al 9 para determinar el cuadrado
    rand2=randint(1,9)  #numero del 1 al 9 para determinar la posicion dentro del cuadrado
    rand3=randint(1,9) #numero del 1 al 9 para determinar el color
    for i in range(0,rand):
        rand1=randint(1,9)  
        rand2=randint(1,10)  
        rand3=randint(1,9)
        if rand2==1:
            rand2=rojo
        if rand2==2:
            rand2=naranja
        if rand2==3:
            rand2=amarillo
        if rand2==4:
            rand2=verde
        if rand2==5:
            rand2=celeste
        if rand2==6:
            rand2=azul
        if rand2==7:
            rand2=morado
        if rand2==8:
            rand2=cafe
        if rand2==9:
            rand2=negro

        elif rand1==1:
            cuad1.lista.remove(0)
            cuad1.lista.insert(rand3,rand2)
            
        elif rand1==2:
            cuad2.lista.insert(rand3,rand2)
            cuad2.lista.remove(0)

        elif rand1==3:
            cuad3.lista.remove(0)
            cuad3.lista.insert(rand3,rand2)

        elif rand1==4:
            cuad4.lista.remove(0)
            cuad4.lista.insert(rand3,rand2)

        elif rand1==5:
            cuad5.lista.remove(0)
            cuad5.lista.insert(rand3,rand2)
      
        elif rand1==6:
            cuad6.lista.remove(0)
            cuad6.lista.insert(rand3,rand2)
       
        elif rand1==7:
            cuad7.lista.remove(0)
            cuad7.lista.insert(rand3,rand2)

        elif rand1==8:
            cuad8.lista.remove(0)
            cuad8.lista.insert(rand3,rand2)
     
        elif rand1==9:
            cuad9.lista.remove(0)
            cuad9.lista.insert(rand3,rand2)
        else:
            pass
    cu=[]
    cu=cu+[cuad1.lista]
    cu=cu+[cuad2.lista]
    cu=cu+[cuad3.lista]
    cu=cu+[cuad4.lista]
    cu=cu+[cuad5.lista]
    cu=cu+[cuad6.lista]
    cu=cu+[cuad7.lista]
    cu=cu+[cuad8.lista]
    cu=cu+[cuad9.lista]
    
    return repetido(cu)
    
            
cuad1=cuadricula()
cuad2=cuadricula()
cuad3=cuadricula()
cuad4=cuadricula()
cuad5=cuadricula()
cuad6=cuadricula()
cuad7=cuadricula()
cuad8=cuadricula()
cuad9=cuadricula()

sec1=cuadricula()
sec2=cuadricula()
sec3=cuadricula()
sec4=cuadricula()
sec5=cuadricula()
sec6=cuadricula()
sec7=cuadricula()
sec8=cuadricula()
sec9=cuadricula()

iniciar()  
