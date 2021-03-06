import pygame
import math
import random
from tlacitko import button

#farby
biela = "#ffffff"
cierna = "#000000"
cervena = "#fc0b03"
zelena = "#03fc0f"
oranzova = "#fa9507"

#slova
lahke_slova = ["PES"]
stredne_slova = ["HARDVER"]
tazke_slova = ["OKULIARE"]

#hinty
hint = ""
hint_viditelnost = False
hint_tlacitko_viditelnost = True

#nastavenia okna
pygame.init()
SIRKA, VYSKA = 800, 500
OKNO = pygame.display.set_mode((SIRKA,VYSKA))
pygame.display.set_caption("Poprava")

#nastavenie hry
FPS = 60
clock = pygame.time.Clock()
hranie = True

#ukaz ronka a zajka
ronko = pygame.image.load("./Obrazky/ronko.png")
zajkoo = pygame.image.load("./Obrazky/zajko.png")

#ukaz ako bude ronko obeseny
obrazky_ronnie = []
for i in range (7):
    obrazok_ronnie = pygame.image.load("./Obrazky/hangman_ronnie_" + str(i) + ".png") 
    obrazky_ronnie.append(obrazok_ronnie)

#ukaz ako bude zajko obeseny
obrazky_zajko = []
for i in range (7):
    obrazok_zajko = pygame.image.load("./Obrazky/hangman_zajko_" + str(i) + ".png") 
    obrazky_zajko.append(obrazok_zajko)

#status popravy
hangman_obrazok = 0

#slova
slova = []
uhadnute = []

#vytvorenie tlacitka s pismenkom
polomer = 20
medzera = 15
pismenka = []
startx = round((SIRKA - (polomer *2 + medzera) * 13)/2)
starty = 400
A = 65

for i in range(26):
    x = startx + medzera * 2 + ((polomer * 2 +medzera) * (i % 13))  #vytvorenie pozicii na Xovej osi
    y = starty + ((i // 13) * (medzera + polomer * 2))              #vytvorenie pozicii na Yovej osi        //-delenie celych cisel = pokial i nebude >= 13 tak tam bude 0
    pismenka.append([x,y, chr(A + i), True])                        #x, y urcu-ju poziciu , chr(A+1) - pismenko ktore tam bude , True - viditelne alebo neviditelne

def zistenie_hintu(vybrane_slovo):
    if vybrane_slovo in lahke_slova:
        if vybrane_slovo == "PES":
            return "Je to velmi caste domace zviera"

    if vybrane_slovo in stredne_slova:
        if vybrane_slovo == "HARDVER":
            return "Fyzicke casti pocitaca"

    if vybrane_slovo in tazke_slova:
        if vybrane_slovo == "OKULIARE":
            return "Ludia ich nosia aby lepsie videli"

def hraj_muzicku_klik():
    pygame.mixer.music.load("./muzicka/klik.wav")
    pygame.mixer.music.play(0)

def hraj_muzicku_vyhra():
    pygame.mixer.music.load("./muzicka/vyhra.wav")
    pygame.mixer.music.play(0)

def get_font_pixel(size):
    return pygame.font.Font("font.ttf", size)

def vyhra_hra(hrac, vybrane_slovo):
    global slova, uhadnute, hangman_obrazok, hint_tlacitko_viditelnost, hint_viditelnost
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        OKNO.fill(biela)

        vyhra_text = get_font_pixel(50).render(hrac + " prezil! ", True, cierna)
        vyhra_text_rect = vyhra_text.get_rect(center=(400,270))
        OKNO.blit(vyhra_text,vyhra_text_rect)

        dalsi_level_tlacitko = button(pos=(250,400), text_input="Dalsi level", font= get_font_pixel(25), base_color = cierna, hovering_color = zelena)
        vypnut_tlacitko = button(pos=(550,400), text_input="Vypnut", font= get_font_pixel(25), base_color = cierna, hovering_color = cervena)

        for tlacitko in [vypnut_tlacitko,dalsi_level_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

        if hrac == "ronko":
            OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))

        if hrac == "zajko":
            OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))


        spravne_slovo_text = get_font_pixel(18).render("Spravne slovo bolo: " + vybrane_slovo, True, cierna)
        spravne_slovo_text_rect = spravne_slovo_text.get_rect(center=(450,190))
        OKNO.blit(spravne_slovo_text, spravne_slovo_text_rect)

        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hraj_muzicku_klik()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if vypnut_tlacitko.check_na_stlacenie(myska_pozicia):
                        hraj_muzicku_klik()
                        pygame.quit()
                    if dalsi_level_tlacitko.check_na_stlacenie(myska_pozicia):
                        hraj_muzicku_klik()
                        slova = []
                        uhadnute = []
                        hangman_obrazok = 0
                        hint_viditelnost = False
                        hint_tlacitko_viditelnost = True
                        for i in range(26):
                            x = startx + medzera * 2 + ((polomer * 2 +medzera) * (i % 13))  
                            y = starty + ((i // 13) * (medzera + polomer * 2))              
                            pismenka.append([x,y, chr(A + i), True])                        
                        vyber_narocnosti()

def prehra_hra(hrac, vybrane_slovo):
    global hangman_obrazok, slova, uhadnute
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        OKNO.fill(biela)
        
        prehra_text = get_font_pixel(50).render(hrac + " zomrel! ", True, cierna)
        prehra_text_rect = prehra_text.get_rect(center=(400,270))
        OKNO.blit(prehra_text,prehra_text_rect)

        vypnut_tlacitko = button(pos=(400,400), text_input="Vypnut", font= get_font_pixel(70), base_color = cierna, hovering_color = cervena)

        for tlacitko in [vypnut_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

        if hrac == "ronko":
            if hangman_obrazok > 6:
                hangman_obrazok = 6
                OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
            else:
                OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
            
        if hrac == "zajko":
            if hangman_obrazok > 6:
                hangman_obrazok = 6
                OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))
            else:
                OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))

        spravne_slovo_text = get_font_pixel(18).render("Spravne slovo bolo: " + vybrane_slovo, True, cierna)
        spravne_slovo_text_rect = spravne_slovo_text.get_rect(center=(450,190))
        OKNO.blit(spravne_slovo_text, spravne_slovo_text_rect)

        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hraj_muzicku_klik()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if vypnut_tlacitko.check_na_stlacenie(myska_pozicia):
                        hraj_muzicku_klik()
                        pygame.quit()
                    
def kresli(hrac, vybrane_slovo):
    global hangman_obrazok, hint_viditelnost, hint_tlacitko_viditelnost
    OKNO.fill(biela)
    myska_pozicia = pygame.mouse.get_pos()
    
    #kreslenie slova
    ukazane_slovo = ""
    for pismenko in vybrane_slovo:
        if pismenko in uhadnute:
            ukazane_slovo += pismenko + " "
        else:
            ukazane_slovo += "_ "
    text = get_font_pixel(20).render(ukazane_slovo, 1, cierna)
    OKNO.blit(text , (300,200))

    #kreslenie tlacitoooook
    for pismenko in pismenka:
        x, y, pis, viditelne = pismenko
        if viditelne:
            pygame.draw.circle(OKNO, cierna, (x,y), polomer, 3)
            text = get_font_pixel(20).render(pis, 1, cierna)
            OKNO.blit(text, (x - text.get_width()/2 ,y - text.get_height()/2))

    if hrac == "ronko":
        if hangman_obrazok > 6:
            hangman_obrazok = 6
            OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
        else:
            OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
        
    if hrac == "zajko":
        if hangman_obrazok > 6:
            hangman_obrazok = 6
            OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))
        else:
            OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))

    hadaj_text = get_font_pixel(35).render("Hadaj slovicko!", True, cierna)
    hadaj_text_rect = hadaj_text.get_rect(center=(500,100))

    OKNO.blit(hadaj_text,hadaj_text_rect)

    if hint_viditelnost == True:
        hint_text = get_font_pixel(15).render( hint , False, cierna)
        hint_text_rect = hint_text.get_rect(center=(250,300))

        OKNO.blit(hint_text,hint_text_rect)

    if hint_tlacitko_viditelnost == True:
        hint_tlacitko = button(pos=(700,250), text_input="HINT", font= get_font_pixel(30), base_color = cierna, hovering_color = zelena)

        for tlacitko in [hint_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hraj_muzicku_klik()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hint_tlacitko_viditelnost == True:
                if hint_tlacitko.check_na_stlacenie(myska_pozicia):
                    hraj_muzicku_klik()
                    hint_viditelnost = True
                    hint_tlacitko_viditelnost = False
            m_x, m_y = myska_pozicia
            for pismenko in pismenka:
                x, y, pis, viditelne = pismenko
                if viditelne:
                    vzdialenost = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if vzdialenost < polomer:
                        hraj_muzicku_klik()
                        pismenko[3] = False
                        uhadnute.append(pis)
                        if pis not in vybrane_slovo:
                            hangman_obrazok += 1 


    pygame.display.update()

def hra(hrac, vybrane_slovo):
    global hangman_obrazok

    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        hadaj_text = get_font_pixel(40).render("Hadaj slovicko!", True, cierna)
        hadaj_text_rect = hadaj_text.get_rect(center=(500,100))

        OKNO.blit(hadaj_text,hadaj_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                  
        kresli(hrac, vybrane_slovo)

        vyhra = True
        for pis in vybrane_slovo:
            if pis not in uhadnute:
                vyhra = False
                break

        if vyhra:
            hraj_muzicku_vyhra()
            vyhra_hra(hrac, vybrane_slovo)

        if hangman_obrazok >= 6:
            prehra_hra(hrac, vybrane_slovo)
             
def vyber_koho_obesit(vybrane_slovo):
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        hra_uvod_text_1 = get_font_pixel(40).render("Koho chce?? obesi???", True, cierna)
        hra_uvod_text_1_rect = hra_uvod_text_1.get_rect(center=(400,100))

        Ronko_tlacitko = button(pos = (200,350), text_input = "Ronnka", font = get_font_pixel(30),base_color = cierna, hovering_color = zelena)
        Zajko_tlacitko = button(pos = (590,350), text_input = "Zajka", font = get_font_pixel(30),base_color = cierna, hovering_color = cervena)

        for tlacitko in [Ronko_tlacitko, Zajko_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)
         
        OKNO.blit(hra_uvod_text_1,hra_uvod_text_1_rect)
        OKNO.blit(ronko,(150, 200))
        OKNO.blit(zajkoo,(550, 200))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hraj_muzicku_klik()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Ronko_tlacitko.check_na_stlacenie(myska_pozicia):
                    hrac = "ronko"
                    hraj_muzicku_klik()
                    hra(hrac, vybrane_slovo)
                if Zajko_tlacitko.check_na_stlacenie(myska_pozicia):
                    hrac = "zajko"
                    hraj_muzicku_klik()
                    hra(hrac, vybrane_slovo)

def vyber_narocnosti():
    global hint
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        vyber_text_narocnost = get_font_pixel(50).render("Ake chces slova", True, cierna)
        vyber_text_narocnost_rect = vyber_text_narocnost.get_rect(center=(400,100))

        lahke_tacitko = button( pos=(400,200), text_input="lahke", font= get_font_pixel(30), base_color = cierna, hovering_color = zelena)
        stredne_tacitko = button( pos=(400,275), text_input="stredne tazke", font= get_font_pixel(30), base_color = cierna, hovering_color = oranzova)
        tazke_tacitko = button( pos=(400,350), text_input="tazke", font= get_font_pixel(30), base_color = cierna, hovering_color = cervena)


        for tlacitko in [lahke_tacitko,stredne_tacitko,tazke_tacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

        OKNO.blit(vyber_text_narocnost,vyber_text_narocnost_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lahke_tacitko.check_na_stlacenie(myska_pozicia):
                    vybrane_slovo = random.choice(lahke_slova)
                    hint = zistenie_hintu(vybrane_slovo)
                    hraj_muzicku_klik()
                    vyber_koho_obesit(vybrane_slovo)
                if stredne_tacitko.check_na_stlacenie(myska_pozicia):
                    vybrane_slovo = random.choice(stredne_slova)
                    hint = zistenie_hintu(vybrane_slovo)
                    hraj_muzicku_klik()
                    vyber_koho_obesit(vybrane_slovo)
                if tazke_tacitko.check_na_stlacenie(myska_pozicia):
                    vybrane_slovo = random.choice(tazke_slova)
                    hint = zistenie_hintu(vybrane_slovo)
                    hraj_muzicku_klik()
                    vyber_koho_obesit(vybrane_slovo)

def main_menu():
    while hranie:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        menu_text = get_font_pixel(100).render("Menu", True, cierna)
        menu_text_rect = menu_text.get_rect(center=(400,100))
        
        hra_tlacitko = button(pos=(400,250), text_input="Hrat", font= get_font_pixel(75), base_color = cierna, hovering_color = zelena)
        vypnut_tlacitko = button(pos=(400,350), text_input="Vypnut", font= get_font_pixel(75), base_color = cierna, hovering_color = cervena)

        for tlacitko in [hra_tlacitko, vypnut_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

        OKNO.blit(menu_text,menu_text_rect)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hraj_muzicku_klik()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hra_tlacitko.check_na_stlacenie(myska_pozicia):
                    hraj_muzicku_klik()
                    vyber_narocnosti()
                if vypnut_tlacitko.check_na_stlacenie(myska_pozicia):
                    hraj_muzicku_klik()
                    pygame.quit() 
                
main_menu()