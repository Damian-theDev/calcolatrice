import pygame
from Dashboard import *

def initialize(screen):
    screen.fill((34, 34, 34))
    
def get_coordinate_finestra():
    return pygame.display.get_surface().get_size()

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

def update_buttons():
    global init_larghezza, init_altezza, lista_bottoni
    
    init_button_y = init_altezza * 0.23
    button_y_inc = (init_altezza - init_button_y) // 5 
    button_x_inc = init_larghezza // 4
    
    lista_bottoni[0] = setup_bottone(font, "(", 0, init_button_y, button_x_inc, init_button_y + button_y_inc)
    lista_bottoni[1] = setup_bottone(font, ")", button_x_inc, init_button_y, button_x_inc * 2, init_button_y + button_y_inc)
    lista_bottoni[2] = setup_bottone(font, "canc", button_x_inc * 2, init_button_y, button_x_inc * 3, init_button_y + button_y_inc)
    lista_bottoni[3] = setup_bottone(font, "/", button_x_inc * 3, init_button_y, button_x_inc * 4, init_button_y + button_y_inc)

    lista_bottoni[4] = setup_bottone(font, "7", 0, init_button_y + button_y_inc, button_x_inc, init_button_y + button_y_inc * 2)
    lista_bottoni[5] = setup_bottone(font, "8", button_x_inc, init_button_y + button_y_inc, button_x_inc * 2, init_button_y + button_y_inc * 2)
    lista_bottoni[6] = setup_bottone(font, "9", button_x_inc * 2, init_button_y + button_y_inc, button_x_inc * 3, init_button_y + button_y_inc * 2)
    lista_bottoni[7] = setup_bottone(font, "x", button_x_inc * 3, init_button_y + button_y_inc, button_x_inc * 4, init_button_y + button_y_inc * 2)

    lista_bottoni[8] = setup_bottone(font, "4", 0, init_button_y + button_y_inc * 2, button_x_inc, init_button_y + button_y_inc * 3)
    lista_bottoni[9] = setup_bottone(font, "5", button_x_inc, init_button_y + button_y_inc * 2, button_x_inc * 2, init_button_y + button_y_inc * 3)
    lista_bottoni[10] = setup_bottone(font, "6", button_x_inc * 2, init_button_y + button_y_inc * 2, button_x_inc * 3, init_button_y + button_y_inc * 3)
    lista_bottoni[11] = setup_bottone(font, "-", button_x_inc * 3, init_button_y + button_y_inc * 2, button_x_inc * 4, init_button_y + button_y_inc * 3)

    lista_bottoni[12] = setup_bottone(font, "1", 0, init_button_y + button_y_inc * 3, button_x_inc, init_button_y + button_y_inc * 4)
    lista_bottoni[13] = setup_bottone(font, "2", button_x_inc, init_button_y + button_y_inc * 3, button_x_inc * 2, init_button_y + button_y_inc * 4)
    lista_bottoni[14] = setup_bottone(font, "3", button_x_inc * 2, init_button_y + button_y_inc * 3, button_x_inc * 3, init_button_y + button_y_inc * 4)
    lista_bottoni[15] = setup_bottone(font, "+", button_x_inc * 3, init_button_y + button_y_inc * 3, button_x_inc * 4, init_button_y + button_y_inc * 4)

    lista_bottoni[16] = setup_bottone(font, "AC", 0, init_button_y + button_y_inc * 4, button_x_inc, init_button_y + button_y_inc * 5)
    lista_bottoni[17] = setup_bottone(font, "0", button_x_inc, init_button_y + button_y_inc * 4, button_x_inc * 2, init_button_y + button_y_inc * 5)
    lista_bottoni[18] = setup_bottone(font, ",", button_x_inc * 2, init_button_y + button_y_inc * 4, button_x_inc * 3, init_button_y + button_y_inc * 5)
    lista_bottoni[19] = setup_bottone(font, "=", button_x_inc * 3, init_button_y + button_y_inc * 4, button_x_inc * 4, init_button_y + button_y_inc * 5)

global init_larghezza, init_altezza, screen

# --- SETUP PYGAME ---
pygame.init()
clock = pygame.time.Clock()
running = True

# --- SETUP SCHERMO ---
init_larghezza, init_altezza = 400, 650
screen = pygame.display.set_mode((init_larghezza, init_altezza), pygame.RESIZABLE)
pygame.display.set_caption('Calcolatrice')

# --- SETUP BOTTONI ---
pygame.font.init()
font = pygame.font.Font(None, 36)  # Font di default, dimensione 36

# --- DASHBOARD SETUP ---
dashboard = Dashboard()

# --- SETUP BOTTONI ---
# coordinate per bottoni
init_button_y = init_altezza * 0.23
button_y_inc = (init_altezza - init_button_y) // 5 
button_x_inc = init_larghezza // 4

# bottoni effettivi                                     --- x inizio      --- y inizio                      --- x fine        --- y fine
# prima riga
bottone_parentesi_aperta = setup_bottone(font,  "(",    0,                init_button_y,                    button_x_inc,     init_button_y + button_y_inc)
bottone_parentesi_chiusa = setup_bottone(font,  ")",    button_x_inc,     init_button_y,                    button_x_inc * 2, init_button_y + button_y_inc)
bottone_canc = setup_bottone(font,              "canc", button_x_inc * 2, init_button_y,                    button_x_inc * 3, init_button_y + button_y_inc)
bottone_divisione = setup_bottone(font,         "/",    button_x_inc * 3, init_button_y,                    button_x_inc * 4, init_button_y + button_y_inc)
# seconda riga
bottone_7 = setup_bottone(font,                 "7",    0,                init_button_y + button_y_inc,     button_x_inc,     init_button_y + button_y_inc * 2)
bottone_8 = setup_bottone(font,                 "8",    button_x_inc,     init_button_y + button_y_inc,     button_x_inc * 2, init_button_y + button_y_inc * 2)
bottone_9 = setup_bottone(font,                 "9",    button_x_inc * 2, init_button_y + button_y_inc,     button_x_inc * 3, init_button_y + button_y_inc * 2)
bottone_moltiplicazione = setup_bottone(font,   "x",    button_x_inc * 3, init_button_y + button_y_inc,     button_x_inc * 4, init_button_y + button_y_inc * 2)
# terza riga
bottone_4 = setup_bottone(font,                 "4",    0,                init_button_y + button_y_inc * 2, button_x_inc,     init_button_y + button_y_inc * 3)
bottone_5 = setup_bottone(font,                 "5",    button_x_inc,     init_button_y + button_y_inc * 2, button_x_inc * 2, init_button_y + button_y_inc * 3)
bottone_6 = setup_bottone(font,                 "6",    button_x_inc * 2, init_button_y + button_y_inc * 2, button_x_inc * 3, init_button_y + button_y_inc * 3)
bottone_sottrazione = setup_bottone(font,       "-",    button_x_inc * 3, init_button_y + button_y_inc * 2, button_x_inc * 4, init_button_y + button_y_inc * 3)
# quarta riga
bottone_1 = setup_bottone(font,                 "1",    0,                init_button_y + button_y_inc * 3, button_x_inc,     init_button_y + button_y_inc * 4)
bottone_2 = setup_bottone(font,                 "2",    button_x_inc,     init_button_y + button_y_inc * 3, button_x_inc * 2, init_button_y + button_y_inc * 4)
bottone_3 = setup_bottone(font,                 "3",    button_x_inc * 2, init_button_y + button_y_inc * 3, button_x_inc * 3, init_button_y + button_y_inc * 4)
bottone_addizione = setup_bottone(font,         "+",    button_x_inc * 3, init_button_y + button_y_inc * 3, button_x_inc * 4, init_button_y + button_y_inc * 4)
# quinta riga
bottone_AC = setup_bottone(font,                "AC",   0,                init_button_y + button_y_inc * 4, button_x_inc,     init_button_y + button_y_inc * 5)
bottone_0 = setup_bottone(font,                 "0",    button_x_inc,     init_button_y + button_y_inc * 4, button_x_inc * 2, init_button_y + button_y_inc * 5)
bottone_virgola = setup_bottone(font,           ",",    button_x_inc * 2, init_button_y + button_y_inc * 4, button_x_inc * 3, init_button_y + button_y_inc * 5)
bottone_uguale = setup_bottone(font,            "=",    button_x_inc * 3, init_button_y + button_y_inc * 4, button_x_inc * 4, init_button_y + button_y_inc * 5)

lista_bottoni = [bottone_parentesi_aperta, bottone_parentesi_chiusa, bottone_canc, bottone_divisione, \
                   bottone_7, bottone_8, bottone_9, bottone_moltiplicazione, \
                   bottone_4, bottone_5, bottone_6, bottone_sottrazione, \
                   bottone_1, bottone_2, bottone_3, bottone_addizione, \
                   bottone_AC, bottone_0, bottone_virgola, bottone_uguale]

# init
initialize(screen)

while running:
    # events section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # resize
        if event.type == pygame.VIDEORESIZE:
            init_larghezza, init_altezza = event.w, event.h
            screen = pygame.display.set_mode((init_larghezza, init_altezza), pygame.RESIZABLE)
            update_buttons()

        # bottone premuto con il mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bottone in lista_bottoni:
                if bottone[0].get_rect(topleft=bottone[1]).collidepoint(event.pos):
                    if bottone[0] == bottone_parentesi_aperta[0]:
                        dashboard.add_valore_stringa_corrente("(")
                    elif bottone[0] == bottone_parentesi_chiusa[0]:
                        dashboard.add_valore_stringa_corrente(")")
                    elif bottone[0] == bottone_canc[0]:
                        dashboard.add_valore_stringa_corrente("canc")
                    elif bottone[0] == bottone_divisione[0]:
                        dashboard.add_valore_stringa_corrente("/")

                    elif bottone[0] == bottone_7[0]:
                        dashboard.add_valore_stringa_corrente(7)
                    elif bottone[0] == bottone_8[0]:
                        dashboard.add_valore_stringa_corrente(8)
                    elif bottone[0] == bottone_9[0]:
                        dashboard.add_valore_stringa_corrente(9)
                    elif bottone[0] == bottone_moltiplicazione[0]:
                        dashboard.add_valore_stringa_corrente("*")

                    elif bottone[0] == bottone_4[0]:
                        dashboard.add_valore_stringa_corrente(4)
                    elif bottone[0] == bottone_5[0]:
                        dashboard.add_valore_stringa_corrente(5)
                    elif bottone[0] == bottone_6[0]:
                        dashboard.add_valore_stringa_corrente(6)
                    elif bottone[0] == bottone_sottrazione[0]:
                        dashboard.add_valore_stringa_corrente("-")
                    
                    elif bottone[0] == bottone_1[0]:
                        dashboard.add_valore_stringa_corrente(1)
                    elif bottone[0] == bottone_2[0]:
                        dashboard.add_valore_stringa_corrente(2)
                    elif bottone[0] == bottone_3[0]:
                        dashboard.add_valore_stringa_corrente(3)
                    elif bottone[0] == bottone_addizione[0]:
                        dashboard.add_valore_stringa_corrente("+")

                    elif bottone[0] == bottone_AC[0]:
                        dashboard.reset()
                    elif bottone[0] == bottone_0[0]:
                        dashboard.add_valore_stringa_corrente(0)
                    elif bottone[0] == bottone_virgola[0]:
                        dashboard.add_valore_stringa_corrente(".")
                    elif bottone[0] == bottone_uguale[0]:
                        print(f'\n--- risultato : {dashboard.calcola_totale()} ---\n')
            print(f'dashboard : {dashboard.get_stringa_corrente()}')

    initialize(screen)

    for superficie, pos in lista_bottoni:
        screen.blit(superficie, pos)

    # update screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS

pygame.quit()