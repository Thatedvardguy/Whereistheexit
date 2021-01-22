#Importerer pygame og sys modulene. Gjor at jeg kan bruke dem i koden.
import pygame, sys

#Starter pygame modulen.
pygame.init()

#Lager skjermstorelsen
vindu_hoyde, vindu_bredde = 750, 750
vindu = pygame.display.set_mode((vindu_bredde,vindu_hoyde))

#Ikonet på vinduet
Ikon = pygame.image.load("joystick.png")

#Navnet på spillet satt på baren overst.
pygame.display.set_caption("Hvor er jeg?")

#Setter et icon øverst til venstre i vinduet.
pygame.display.set_icon(Ikon)

#Lager en klokke og setter den i variablen "Skjermbilder"
skjermbilder = pygame.time.Clock()

    #Bakgrunner
#Setter png filer, som skal brukes som bakgrunner i spillet, til forskjellige variabler. 
START = pygame.image.load("start.png")
CROSS = pygame.image.load("xCross.png")

CAVE1 = pygame.image.load("xCave1.png")
CAVE2 = pygame.image.load("xCave2.png")
CAVE3 = pygame.image.load("xCave3.png")
CAVE4 = pygame.image.load("xCave4.png")

CROSS = pygame.image.load("xCross.png")
HALL1 = pygame.image.load("xHall1.png")
HALL2 = pygame.image.load("XHall2.png")

T1 = pygame.image.load("xT1.png")
T2 = pygame.image.load("xT2.png")
T3 = pygame.image.load("xT3.png")
T4 = pygame.image.load("xT4.png")

eksit = pygame.image.load("End.png")
tapskjerm = pygame.image.load("tapskjerm.png")

    #True/False statements
"""
Hvert false og true forteller om et rom i spillet. Når en av dem blir true, 
så aktiverer dette et if statement som fremkaller en funksjon for rommet i spillet.
Noen ganger fremkaller det også funksjonen *losscond som sjekker om skjellethodet treffer helten.
"""
atstart = True
atfirstcross = False
greenpath = [False, False, False, False]
bluepath = [False, False, False, False, False, False, False]
yellowpath = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
Slutt = False

enemyact = False
loss = False

    #Karakterer
#Karakteren du spiller, dens posisjon på vinduet, og en rektangel rundt den. 
helt_x = 350
helt_y = 350
helt_surf = pygame.image.load("xhelt.png")
helt_rect = helt_surf.get_rect(center=(helt_x,helt_y))

#Verdier for hvor karakteren skal bli satt når han går til et nytt rom
heltopp = 20
heltned = 730
helthoyre = 730
heltvenstre = 20
heltntrl = 350

playerspeed = 1.5


#Fienden
enemy_x = 150
enemy_y = 150
enemy_surf = pygame.image.load("CursedSkullRight.png")
enemy_rect = enemy_surf.get_rect(center=(enemy_x,enemy_y))

enemyspeed = 2

#Funksjoner for alle rommene i spillet
def startbc():
    global helt_x, helt_y, atfirstcross, atstart, enemyact
    vindu.blit(START, (0,0))
    if helt_y >= vindu_hoyde:
        atstart = False #Når helten beveger seg ut av rommet så blir if setningen som sjekker at du er i rommet false og den andre rommet blir true.
        atfirstcross = True 
        helt_x = heltntrl #Flytter helten til riktig side av skjermen i forhold til der hvor han gikk.
        helt_y = heltopp
        enemyact = True #Når true så blir fienden tegnet på skjermen.
#Gjør at helten ikke kan bevege seg ut av skjermen.
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10
    if helt_x <= 0:
       helt_x = helt_x + 10
    if helt_y <= 0:
       helt_y = helt_y + 10        

        
def crossroads():
    global helt_x, helt_y, atfirstcross, atstart, enemyact
    vindu.blit(CROSS, (0,0))
    if helt_y <= 0:
        atfirstcross = False
        atstart = True
        helt_x = heltntrl
        helt_y = heltned
        enemyact = False
        
    if helt_y >= vindu_hoyde:
        atfirstcross = False
        bluepath[0] = True
        helt_x = heltntrl
        helt_y = heltopp
        
    if helt_x <= 0:
        atfirstcross = False
        greenpath[0] = True
        helt_x = helthoyre
        helt_y = heltntrl
        
    if helt_x >= vindu_bredde:
        atfirstcross = False
        yellowpath[0] = True
        helt_x = heltvenstre
        helt_y = heltntrl        
        enemyact = False

#Funksjoner for rom i spillet
def GREENPATH0():
    global helt_x, helt_y, atfirstcross, greenpath, enemyact
    vindu.blit(T1,(0,0))
    if helt_x >= vindu_bredde:
        greenpath[0] = False
        atfirstcross = True
        helt_x = heltvenstre
        helt_y = heltntrl

    if helt_y <= 0:
        greenpath[0] = False
        greenpath[1] = True
        helt_x = heltntrl
        helt_y = heltned
        
    if helt_y >= vindu_hoyde:
        greenpath[0] = False
        greenpath[2] = True
        helt_x = heltntrl
        helt_y = heltopp
 
    if helt_x <= 0:
       helt_x = helt_x + 10
    
    
def GREENPATH1():
    global helt_x, helt_y
    vindu.blit(CAVE1, (0,0))
    if helt_y >= vindu_hoyde:
        greenpath[1] = False
        greenpath[0] = True
        helt_x = heltntrl
        helt_y = heltopp
        
    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_y <= 0:
       helt_y = helt_y + 10  
       
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10

def GREENPATH2():
    global helt_x, helt_y, greenpath
    vindu.blit(HALL2, (0,0))
    if helt_y >= vindu_hoyde:
        greenpath[2] = False
        greenpath[3] = True
        helt_x = heltntrl
        helt_y = heltopp
        
    if helt_y <= 0:
        greenpath[2] = False
        greenpath[0] = True
        helt_x = heltntrl
        helt_y = heltned
        
    if helt_x <= 0:
       helt_x = helt_x + 10
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10
        
        
def GREENPATH3():
    global helt_x, helt_y, greenpath
    vindu.blit(CAVE2,(0,0))
    if helt_y <= 0:
        greenpath[3] = False
        greenpath[2] = True
        helt_x = heltntrl
        helt_y = heltned

    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10

    if helt_x <= 0:
       helt_x = helt_x + 10



def BLUEPATH0():
    global helt_x, helt_y, bluepath, atfirstcross, enemyact
    vindu.blit(T2,(0,0))
    if helt_y <= 0:
        bluepath[0] = False
        atfirstcross = True
        helt_x = heltntrl
        helt_y = heltned
        enemyact = True

    if helt_x <= 0:
        bluepath[0] = False
        bluepath[1] = True
        helt_x = helthoyre
        helt_y = heltntrl

    if helt_y >= vindu_hoyde:
        bluepath[0] = False
        bluepath[2] = True
        helt_x = heltntrl
        helt_y = heltopp

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10


def BLUEPATH1():
    global helt_x, helt_y, bluepath
    vindu.blit(CAVE3, (0,0))
    if helt_x >= vindu_bredde:
        bluepath[1] = False
        bluepath[0] = True
        helt_x = heltvenstre
        helt_y = heltntrl

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10

    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_y <= 0:
       helt_y = helt_y + 10

def BLUEPATH2():
    global helt_x, helt_y, bluepath
    vindu.blit(HALL2, (0,0))
    if helt_y <= 0:
        bluepath[2] = False
        bluepath[0] = True
        helt_x = heltntrl
        helt_y = heltned

        
    if helt_y >= vindu_hoyde:
        bluepath[2] = False
        bluepath[3] = True
        helt_x = heltntrl
        helt_y = heltopp

    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10


def BLUEPATH3():
    global helt_x, helt_y, bluepath
    vindu.blit(HALL2, (0,0))
    if helt_y <= 0:
        bluepath[3] = False
        bluepath[2] = True
        helt_x = heltntrl
        helt_y = heltned
        
    if helt_y >= vindu_hoyde:
        bluepath[3] = False
        bluepath[4] = True
        helt_x = heltntrl
        helt_y = heltopp

    if helt_x <= 0:
       helt_x = helt_x + 10
 
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10


def BLUEPATH4():
    global helt_x, helt_y, bluepath
    vindu.blit(T3, (0,0))
    if helt_x >= vindu_bredde:
        bluepath[4] = False
        bluepath[6] = True
        helt_x = heltvenstre
        helt_y = heltntrl
    if helt_x <= 0:
        bluepath[4] = False
        bluepath[5] = True
        helt_x = helthoyre
        helt_y = heltntrl

    if helt_y <= 0:
        bluepath[4] = False
        bluepath[3] = True
        helt_x = heltntrl
        helt_y = heltned

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10


def BLUEPATH5():
    global helt_x, helt_y, bluepath
    vindu.blit(CAVE3, (0,0))    
    if helt_x >= vindu_bredde:
        bluepath[5] = False
        bluepath[4] = True
        helt_x = heltvenstre
        helt_y = heltntrl

def BLUEPATH6():
    global helt_x, helt_y, bluepath
    vindu.blit(CAVE4, (0,0))
    if helt_x <= 0:
        bluepath[6] = False
        bluepath[4] = True
        helt_x = helthoyre
        helt_y = heltntrl

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10

    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_y <= 0:
       helt_y = helt_y + 10

def YELLOWPATH0():
    global helt_x, helt_y, yellowpath, atfirstcross, enemyact
    vindu.blit(T3, (0,0))
    if helt_x <= 0:
        yellowpath[0] = False
        atfirstcross = True
        helt_x = helthoyre
        helt_y = heltntrl
        enemyact = True

    if helt_x >= vindu_bredde:
        yellowpath[0] = False
        yellowpath[11] = True
        helt_x = heltvenstre
        helt_y = heltntrl
        enemyact = True

    if helt_y <= 0:
        yellowpath[0] = False
        yellowpath[1] = True
        helt_x = heltntrl
        helt_y = heltned

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10


def YELLOWPATH1():
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(HALL2, (0,0))
    if helt_y >= vindu_hoyde:
        yellowpath[1] = False
        yellowpath[0] = True
        helt_x = heltntrl
        helt_y = heltopp
        
    if helt_y <= 0:
        yellowpath[1] = False
        yellowpath[2] = True
        helt_x = heltntrl
        helt_y = heltned
        enemyact = True

    if helt_x <= 0:
       helt_x = helt_x + 10
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10


def YELLOWPATH2():
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(HALL2, (0,0))
    if helt_y >= vindu_hoyde:
        yellowpath[2] = False
        yellowpath[1] = True
        helt_x = heltntrl
        helt_y = heltopp
        enemyact = False
        
    if helt_y <= 0:
        yellowpath[2] = False
        yellowpath[3] = True
        helt_x = heltntrl
        helt_y = heltned
 
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10
    if helt_x <= 0:
       helt_x = helt_x + 10
        

def YELLOWPATH3():
    global helt_x, helt_y, yellowpath
    vindu.blit(T4,(0,0))
    if helt_x <= 0:
        yellowpath[3] = False
        yellowpath[4] = True
        helt_x = helthoyre
        helt_y = heltntrl

    if helt_x >= vindu_bredde:
        yellowpath[3] = False
        yellowpath[5] = True
        helt_x = heltvenstre
        helt_y = heltntrl
        
    if helt_y >= vindu_hoyde:
        yellowpath[3] = False
        yellowpath[2] = True
        helt_x = heltntrl
        helt_y = heltopp

    if helt_y <= 0:
       helt_y = helt_y + 10

def YELLOWPATH4():
    global helt_x, helt_y, yellowpath
    vindu.blit(CAVE3,(0,0))
    if helt_x >= vindu_bredde:
        yellowpath[4] = False
        yellowpath[3] = True
        helt_x = heltvenstre
        helt_y = heltntrl
    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10

    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_y <= 0:
       helt_y = helt_y + 10

def YELLOWPATH5():
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(CAVE4,(0,0))
    if helt_x <= 0:
        yellowpath[5] = False
        yellowpath[3] = True
        helt_x = helthoyre
        helt_y = heltntrl
        enemyact = True
    if helt_y <= 0:
       helt_y = helt_y + 10
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10
    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10
       

def YELLOWPATH6():    
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(CROSS,(0,0))
    if helt_x <= 0:
        yellowpath[6] = False
        yellowpath[7] = True
        helt_x = helthoyre
        helt_y = heltntrl
    if helt_x >= vindu_bredde:
        yellowpath[6] = False
        yellowpath[9] = True
        helt_x = heltvenstre
        helt_y = heltntrl
    if helt_y >= vindu_hoyde:
        yellowpath[6] = False
        yellowpath[8] = True
        helt_x = heltntrl
        helt_y = heltopp
        enemyact = False
    if helt_y <= 0:
        yellowpath[6] = False
        yellowpath[12] = True
        helt_x = heltntrl
        helt_y = heltned

def YELLOWPATH7():
    global helt_x, helt_y, yellowpath
    vindu.blit(CAVE3,(0,0))
    if helt_x >= vindu_bredde:
        yellowpath[7] = False
        yellowpath[6] = True
        helt_x = heltvenstre
        helt_y = heltntrl

def YELLOWPATH8():
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(CAVE2,(0,0))    
    if helt_y <= 0:
        yellowpath[8] = False
        yellowpath[6] = True
        helt_x = heltntrl
        helt_y = heltned
        enemyact = True
    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10

    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_y <= 0:
       helt_y = helt_y + 10
def YELLOWPATH9():
    global helt_x, helt_y, yellowpath
    vindu.blit(HALL1, (0,0))    
    if helt_x >= vindu_bredde:
        yellowpath[9] = False
        yellowpath[10] = True
        helt_x = heltvenstre
        helt_y = heltntrl

    if helt_x <= 0:
        yellowpath[9] = False
        yellowpath[6] = True
        helt_x = helthoyre
        helt_y = heltntrl
    if helt_y <= 0:
       helt_y = helt_y + 10
    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10


def YELLOWPATH10():
    global helt_x, helt_y, yellowpath
    vindu.blit(CAVE4, (0,0))  
    if helt_x <= 0:
        yellowpath[10] = False
        yellowpath[9] = True
        helt_x = helthoyre
        helt_y = heltntrl
    if helt_y <= 0:
       helt_y = helt_y + 10
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10

    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10


def YELLOWPATH11():
    global helt_x, helt_y, yellowpath, enemyact
    vindu.blit(HALL1,(0,0))
    if helt_x <= 0:
        yellowpath[11] = False
        yellowpath[0] = True
        helt_x = helthoyre
        helt_y = heltntrl
        enemyact = False
    if helt_x >= vindu_bredde:
        yellowpath[11] = False
        yellowpath[12] = True
        helt_x = heltvenstre
        helt_y = heltntrl
    if helt_y >= vindu_hoyde:
       helt_y = helt_y -10
    if helt_y <= 0:
       helt_y = helt_y + 10

def YELLOWPATH12():
    global helt_x, helt_y, yellowpath
    vindu.blit(T2,(0,0))
    if helt_x <= 0:
        yellowpath[12] = False
        yellowpath[11] = True
        helt_x = helthoyre
        helt_y = heltntrl
        
    if helt_y <= 0:
        yellowpath[12] = False
        yellowpath[13] = True
        helt_x = heltntrl
        helt_y = heltned
    
    if helt_y >= vindu_hoyde:
        yellowpath[12] = False
        yellowpath[6] = True
        helt_x = heltntrl
        helt_y = heltopp
    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10
        
def YELLOWPATH13():
    global helt_x, helt_y, yellowpath, Slutt, enemyact
    vindu.blit(HALL2, (0,0))
    if helt_y >= vindu_hoyde:
        yellowpath[13] = False
        yellowpath[12] = True
        helt_x = heltntrl
        helt_y = heltopp

    if helt_y <= 0:
        yellowpath[13] = False
        Slutt = True
        helt_x = 400
        helt_y = 200
        enemyact = False
    if helt_x <= 0:
       helt_x = helt_x + 10

    if helt_x >= vindu_bredde:
       helt_x = helt_x - 10


def EXIT():
    vindu.blit(eksit, (0,0))

#Sjekker om fienden er ca innenfor koordinatene til helten.
def losscond():
    global loss
    if (helt_x+23) >= (enemy_x-13) and (helt_x-23) <= (enemy_x+13) and (helt_y+38) >= (enemy_y-14) and (helt_y-38) <= (enemy_y+14):
        loss = True

    #Gameloopen
#Looper slik at det som er på skjermen blir tegnet om og om igjen.
while True:
    for event in pygame.event.get(): #Får pygame til å lete etter events.
        if event.type == pygame.QUIT: #Hvis bruker trykker på X knappen, så quiter de ut av pygame, og koden slutter.
            pygame.quit()
            sys.exit()
#Kaller fram funksjonene for rommene
    if atstart == True:
        startbc()
    if atfirstcross == True:
        crossroads()
        losscond()
    if greenpath[0] == True:
        GREENPATH0()
        losscond()
    if greenpath[1] == True:
        GREENPATH1()
        losscond()
    if greenpath[2] == True:
        GREENPATH2()
        losscond()
    if greenpath[3] == True:
        GREENPATH3()
        losscond()
    if bluepath[0] == True:
       BLUEPATH0() 
       losscond()
    if bluepath[1] == True:
        BLUEPATH1()
        losscond()
    if bluepath[2] == True:
        BLUEPATH2()
        losscond()
    if bluepath[3] == True:
        BLUEPATH3()
        losscond()
    if bluepath[4] == True:
        BLUEPATH4()
        losscond()
    if bluepath[5] == True:
        BLUEPATH5()
        losscond()
    if bluepath[6] == True:
        BLUEPATH6()
        losscond()
    if yellowpath[0] == True:
        YELLOWPATH0()
    if yellowpath[1] == True:
        YELLOWPATH1()
    if yellowpath[2] == True:
        YELLOWPATH2()
        losscond()
    if yellowpath[3] == True:
        YELLOWPATH3()
        losscond()
    if yellowpath[4] == True:
        YELLOWPATH4()
        losscond()
    if yellowpath[5] == True:
        YELLOWPATH5()
        losscond()
    if yellowpath[6] == True:
        YELLOWPATH6()
        losscond()
    if yellowpath[7] == True:
        YELLOWPATH7()
        losscond()
    if yellowpath[8] == True:
        YELLOWPATH8()
    if yellowpath[9] == True:
        YELLOWPATH9()
        losscond()
    if yellowpath[10] == True:
        YELLOWPATH10()
        losscond()
    if yellowpath[11] == True:
        YELLOWPATH11()
        losscond()
    if yellowpath[12] == True:
        YELLOWPATH12()
        losscond()
    if yellowpath[13] == True:
        YELLOWPATH13()
        losscond()
    if Slutt == True:
        EXIT()
#Gjør at man kan se fienden.
    if enemyact == True:
        vindu.blit(enemy_surf, (enemy_x, enemy_y))

    vindu.blit(helt_surf, (helt_x, helt_y))
#Denne sjekker om loss == False, og loss == False når helten har koordinater
#som er innenfor koordinatene til fienden. Det er dette som er funksjonen losscond.
    if loss == False:
        if enemy_y == 150:
            enemy_x += 5
            enemy_surf = pygame.image.load("CursedSkullRight.png")
    
        if enemy_x == 600:
            enemy_y += 5
            enemy_surf = pygame.image.load("CursedSkullDown.png")
    
        if enemy_y == 600:
            enemy_x -= 5
            enemy_surf = pygame.image.load("CursedSkullLeft.png")
    
        if enemy_x == 150:
            enemy_y -= 5
            enemy_surf = pygame.image.load("CursedSkullUp.png")
       
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            helt_y += playerspeed
        if key[pygame.K_d]:
            helt_x += playerspeed
        if key[pygame.K_w]:
            helt_y -= playerspeed
        if key[pygame.K_a]:
            helt_x -= playerspeed
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    #Hvis man er inærheten av hodet så viser den tapskjermen.
    elif loss == True:
        vindu.blit(tapskjerm, (0,0))

    pygame.display.update() #Oppdaterer skjermen.
    skjermbilder.tick(240) #Passer på at det er 240 skjermbilder som vises per sekund. Dette gjør at while løkken ikke går for raskt.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    