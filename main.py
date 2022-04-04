import pygame
from tlacitko import button

def get_font(size):
    return pygame.font.Font("font.ttf", size)

def hra(x):
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(pozadie_biela)
        if x == 0:
            OKNO.blit(obrazky_ronnie[hangman_obrazok], (1,1))
        elif x == 1:
            OKNO.blit(obrazky_zajko[hangman_obrazok], (1,1))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def vyber_koho_obesit():
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(pozadie_siva)

        hra_uvod_text_1 = get_font(40).render("Koho chceš obesiť?", True, "#FFFFFF")
        hra_uvod_text_1_rect = hra_uvod_text_1.get_rect(center=(400,100))

        Ronko_tlacitko = button(pos = (200,350), text_input = "Ronnka", font = get_font(30),base_color = tlacitko_1_base, hovering_color = tlacitko_1_hovering)
        Zajko_tlacitko = button(pos = (590,350), text_input = "Zajka", font = get_font(30),base_color = tlacitko_1_base, hovering_color = tlacitko_1_hovering)

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
                    x = 0
                    hra(x)
                if Zajko_tlacitko.check_na_stlacenie(myska_pozicia):
                    x = 1
                    hra(x)
                    

def main_menu():
    while True:
        myska_pozicia = pygame.mouse.get_pos()
        clock.tick(FPS)
        OKNO.fill(pozadie_siva)

        menu_text = get_font(100).render("Menu", True, "#FFFFFF")
        menu_text_rect = menu_text.get_rect(center=(400,100))
        menu_IG = get_font(25).render("IG: Martin.lmi",True,"#57d7d9")
        menu_IG_rect = menu_text.get_rect(center=(200,525))

        hra_tlacitko = button(pos=(400,250), text_input="Hrat", font= get_font(75), base_color = tlacitko_1_base, hovering_color = tlacitko_1_hovering)
        vypnut_tlacitko = button(pos=(400,350), text_input="Vypnut", font= get_font(75), base_color = tlacitko_1_base, hovering_color = tlacitko_1_hovering)

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
                    vyber_koho_obesit()
                
                if vypnut_tlacitko.check_na_stlacenie(myska_pozicia):
                    pygame.quit()
                    

#farby
pozadie_siva = "#858282"
pozadie_biela = "#ffffff"
tlacitko_1_base = "#454141"
tlacitko_1_hovering = "#1f1d1d"

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

hangman_obrazok = 0

main_menu()