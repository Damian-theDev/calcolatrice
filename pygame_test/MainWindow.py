import pygame
from Dashboard import *

def initialize(screen):
    screen.fill((34, 34, 34))
    
def get_coordinate_finestra():
    return pygame.display.get_surface().get_size()

# pygame setup
pygame.init()

clock = pygame.time.Clock()
running = True

# window setup
global init_larghezza, init_altezza, screen

init_larghezza, init_altezza = 400, 650
screen = pygame.display.set_mode((init_larghezza, init_altezza), pygame.RESIZABLE)
pygame.display.set_caption('Calcolatrice')

# button setup
pygame.font.init()
font = pygame.font.Font(None, 36)  # Font di default, dimensione 36

def setup_bottone(font, text, surface_init_x, surface_init_y, surface_final_x, surface_final_y):
    surface = pygame.Surface((surface_final_x - surface_init_x, surface_final_y - surface_init_y))  # Dimensioni della superficie
    surface.fill((69, 69, 69))  # Colore della superficie

    # Disegna il bordo
    pygame.draw.rect(surface, (255, 255, 255), surface.get_rect(), 1)  # Colore bianco, spessore 3

    # testo
    text = font.render(str(text), True, (255, 255, 255))  # Anti-aliasing attivato
    text_rect = text.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))  # Centra il testo
    surface.blit(text, text_rect)  # Disegna il testo sulla superficie

    return surface, (surface_init_x, surface_init_y)

# coordinate per bottoni
init_button_y = init_altezza * 0.23
button_y_inc = (init_altezza - init_button_y) // 5 
button_x_inc = init_larghezza // 4

# bottoni effettivi
# prima riga
bottone_parentesi_aperta = setup_bottone(font, "(", 0, init_button_y, button_x_inc, init_button_y + button_y_inc)
bottone_parentesi_chiusa = setup_bottone(font, ")", button_x_inc, init_button_y, button_x_inc * 2, init_button_y + button_y_inc)
bottone_canc = setup_bottone(font, "canc", button_x_inc * 2, init_button_y, button_x_inc * 3, init_button_y + button_y_inc)
bottone_divisione = setup_bottone(font, "/", button_x_inc * 3, init_button_y, button_x_inc * 4, init_button_y + button_y_inc)
# seconda riga
bottone_7 = setup_bottone(font, "7", 0, init_button_y + button_y_inc, button_x_inc, init_button_y + button_y_inc * 2)
bottone_8 = setup_bottone(font, "8", button_x_inc, init_button_y + button_y_inc, button_x_inc * 2, init_button_y + button_y_inc * 2)
bottone_9 = setup_bottone(font, "9", button_x_inc * 2, init_button_y + button_y_inc, button_x_inc * 3, init_button_y + button_y_inc * 2)
bottone_moltiplicazione = setup_bottone(font, "X", button_x_inc * 3, init_button_y + button_y_inc, button_x_inc * 4, init_button_y + button_y_inc * 2)
# terza riga
# quarta riga
# quinta riga
bottone_AC = setup_bottone(font, "AC", 0, init_button_y + button_y_inc * 4, button_x_inc, init_button_y + button_y_inc * 5)
bottone_uguale = setup_bottone(font, "=", button_x_inc * 3, init_button_y + button_y_inc * 4, button_x_inc * 4, init_button_y + button_y_inc * 5)

lista_superfici = [bottone_parentesi_aperta, bottone_parentesi_chiusa, bottone_canc, bottone_divisione, \
                   bottone_7, bottone_8, bottone_9, bottone_moltiplicazione, \
                   \
                   bottone_AC, bottone_uguale]

# dashboard setup
dashboard = Dashboard()

# init
initialize(screen)

while running:
    # events section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # bottone premuto con il mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if bottone_parentesi_aperta[0].get_rect(topleft=bottone_parentesi_aperta[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente("(")
            if bottone_parentesi_chiusa[0].get_rect(topleft=bottone_parentesi_chiusa[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente(")")
            if bottone_canc[0].get_rect(topleft=bottone_canc[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente("canc")
            if bottone_divisione[0].get_rect(topleft=bottone_divisione[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente("/")
            
            if bottone_7[0].get_rect(topleft=bottone_7[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente(7)
            if bottone_8[0].get_rect(topleft=bottone_8[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente(8)
            if bottone_9[0].get_rect(topleft=bottone_9[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente(9)
            if bottone_moltiplicazione[0].get_rect(topleft=bottone_moltiplicazione[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente("*")
            
            if bottone_AC[0].get_rect(topleft=bottone_AC[1]).collidepoint(event.pos):
                dashboard.add_valore_stringa_corrente("AC")
            if bottone_uguale[0].get_rect(topleft=bottone_uguale[1]).collidepoint(event.pos):
                dashboard.calcola()

            print(dashboard.get_stringa_corrente())

    # RENDER YOUR GAME HERE
    initialize(screen)

    for superficie, pos in lista_superfici:
        screen.blit(superficie, pos)
        # TODO: reimposta grandezza e posizione dei bottoni

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
