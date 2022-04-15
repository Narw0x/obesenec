import pygame
import math
from tlacitko import button


def get_font_pixel(size):
    return pygame.font.Font("font.ttf", size)

def kresli(hrac):
    OKNO.fill(biela)

    #kreslenie tlacitoooook
    for pismenko in pismenka:
        x, y, pis, viditelne = pismenko
        if viditelne:
            pygame.draw.circle(OKNO, cierna, (x,y), polomer, 3)
            text = get_font_pixel(20).render(pis, 1, cierna)
            OKNO.blit(text, (x - text.get_width()/2 ,y - text.get_height()/2))

    if hrac == 0:
        OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
    elif hrac == 1:
        OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))

    pygame.display.update()

def hra(hrac, slova):
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        kresli(hrac)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = myska_pozicia
                for pismenko in pismenka:
                    x, y, pis, viditelne = pismenko
                    if viditelne:
                        vzdialenost = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if vzdialenost < polomer:
                            pismenko[3] = False




def vyber_koho_obesit(slova):
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        hra_uvod_text_1 = get_font_pixel(40).render("Koho chceš obesiť?", True, cierna)
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
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Ronko_tlacitko.check_na_stlacenie(myska_pozicia):
                    hrac = 0
                    hra(hrac, slova)
                if Zajko_tlacitko.check_na_stlacenie(myska_pozicia):
                    hrac = 1
                    hra(hrac, slova)

def vyber_narocnosti():
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        vyber_text_narocnost = get_font_pixel(50).render("Ake chces slova", True, cierna)
        vyber_text_narocnost_rect = vyber_text_narocnost.get_rect(center=(400,100))

        lahke_tacitko = button( pos=(400,200), text_input="lahke", font= get_font_pixel(30), base_color = cierna, hovering_color = zelena)
        stredne_tacitko = button( pos=(400,275), text_input="stredne tazke", font= get_font_pixel(30), base_color = cierna, hovering_color = zlta)
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
                    slova = lahke_slova
                    vyber_koho_obesit(slova)
                if stredne_tacitko.check_na_stlacenie(myska_pozicia):
                    slova = stredne_slova
                    vyber_koho_obesit(slova)
                if tazke_tacitko.check_na_stlacenie(myska_pozicia):
                    slova = tazke_slova
                    vyber_koho_obesit(slova)


def main_menu():
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(biela)

        menu_text = get_font_pixel(100).render("Menu", True, cierna)
        menu_text_rect = menu_text.get_rect(center=(400,100))
        menu_IG = get_font_pixel(25).render("IG: Martin.lmi",True,"#57d7d9")
        menu_IG_rect = menu_text.get_rect(center=(200,525))

        hra_tlacitko = button(pos=(400,250), text_input="Hrat", font= get_font_pixel(75), base_color = cierna, hovering_color = zelena)
        vypnut_tlacitko = button(pos=(400,350), text_input="Vypnut", font= get_font_pixel(75), base_color = cierna, hovering_color = cervena)

        for tlacitko in [hra_tlacitko, vypnut_tlacitko]:
            tlacitko.zmenenie_farby(myska_pozicia)
            tlacitko.aktualizuj(OKNO)

        OKNO.blit(menu_text,menu_text_rect)
        OKNO.blit(menu_IG,menu_IG_rect)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hra_tlacitko.check_na_stlacenie(myska_pozicia):
                    vyber_narocnosti()
                
                if vypnut_tlacitko.check_na_stlacenie(myska_pozicia):
                    pygame.quit()
                    

#farby
biela = "#ffffff"
cierna = "#000000"
cervena = "#fc0b03"
zelena = "#03fc0f"
zlta = "#fff70d"

#slova
lahke_slova = ["python", "zajac", "pes", "dom"]
stredne_slova = ["programovanie", "batoh", "radost", "monitor"]
tazke_slova = ["magnetka", "horcik", "mineralka", "opatrovatelka"]

#nastavenia okna
pygame.init()
SIRKA, VYSKA = 800, 500
OKNO = pygame.display.set_mode((SIRKA,VYSKA))
pygame.display.set_caption("Poprava")

#nastavenie hry
FPS = 60
clock = pygame.time.Clock()

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

#vytvorenie tlacitka s pismenkom
polomer = 20
medzera = 15
pismenka = []
startx = round((SIRKA - (polomer *2 + medzera) * 13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + medzera * 2 + ((polomer * 2 +medzera) * (i % 13))
    y = starty + ((i // 13) * (medzera + polomer * 2))
    pismenka.append([x,y, chr(A + i), True])


main_menu()