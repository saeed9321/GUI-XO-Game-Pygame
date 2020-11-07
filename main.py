import pygame

pygame.init()

WIN = pygame.display.set_mode((400,400))
pygame.display.set_caption("XO Game")
BG1 = pygame.image.load('assets/background-black.png').convert()
BG = pygame.image.load('assets/white_background.png').convert()
x_img = pygame.transform.scale(pygame.image.load('assets/x.png'), (100,100))
o_img = pygame.transform.scale(pygame.image.load('assets/o.png'), (100,100))
main_font = pygame.font.SysFont('comicsansms', 72)
turn = 0
x = ""
o = ""
winner = ""
finished = False



WIN.blit(BG, (0, 0))

pygame.draw.line(WIN, (0,0,0), (133,20), (133,380), 2)
pygame.draw.line(WIN, (0,0,0), (267,20), (267,380), 2)
pygame.draw.line(WIN, (0,0,0), (20,133), (380,133), 2)
pygame.draw.line(WIN, (0,0,0), (20,267), (380,267), 2)

rect1 = pygame.draw.rect(BG, (255,255,255), (0,0,133, 133))
rect2 = pygame.draw.rect(BG, (255,255,255), (133,0,134, 132))
rect3 = pygame.draw.rect(BG, (255,255,255), (267,0,135, 134))
rect4 = pygame.draw.rect(BG, (255,255,255), (0,133,132, 132))
rect5 = pygame.draw.rect(BG, (255,255,255), (133,133,132, 135))
rect6 = pygame.draw.rect(BG, (255,255,255), (267,133,134, 133))
rect7 = pygame.draw.rect(BG, (255,255,255), (0,267,134, 131))
rect8 = pygame.draw.rect(BG, (255,255,255), (133,267,135, 137))
rect9 = pygame.draw.rect(BG, (255,255,255), (267,267,132, 136))

def clicked(pos):
    global turn, x, o
    turn += 1
    if turn % 2 == 0:
        selection = o_img
        letter = "o"
    else:
        selection = x_img
        letter = "x"

    if rect1.collidepoint(pos):
        WIN.blit(selection, (20, 10))
        if letter == "x": x+=("1")
        else: o+=("1")
    if rect2.collidepoint(pos):
        WIN.blit(selection, (153, 10))
        if letter == "x": x+=("2")
        else: o+=("2")
    if rect3.collidepoint(pos):
        WIN.blit(selection, (287, 10))
        if letter == "x": x+=("3")
        else: o+=("3")
    if rect4.collidepoint(pos):
        WIN.blit(selection, (20, 143))
        if letter == "x": x+=("4")
        else: o+=("4")
    if rect5.collidepoint(pos):
        WIN.blit(selection, (153, 143))
        if letter == "x": x+=("5")
        else: o+=("5")
    if rect6.collidepoint(pos):
        WIN.blit(selection, (287, 143))
        if letter == "x": x+=("6")
        else: o+=("6")
    if rect7.collidepoint(pos):
        WIN.blit(selection, (20, 287))
        if letter == "x": x+=("7")
        else: o+=("7")
    if rect8.collidepoint(pos):
        WIN.blit(selection, (153, 287))
        if letter == "x": x+=("8")
        else: o+=("8")
    if rect9.collidepoint(pos):
        WIN.blit(selection, (287, 287))
        if letter == "x": x+=("9")
        else: o+=("9")


def check():
    global winner
    if "1" in x and "2" in x and "3" in x: winner = "x"
    elif "4" in x and "5" in x and "6" in x: winner = "x"
    elif "7" in x and "8" in x and "9" in x: winner = "x"
    elif "1" in x and "4" in x and "7" in x: winner = "x"
    elif "2" in x and "5" in x and "8" in x: winner = "x"
    elif "3" in x and "6" in x and "9" in x: winner = "x"
    elif "1" in x and "5" in x and "9" in x: winner = "x"
    elif "3" in x and "5" in x and "7" in x: winner = "x"
    elif "1" in o and "2" in o and "3" in o: winner = "o"
    elif "4" in o and "5" in o and "6" in o: winner = "o"
    elif "7" in o and "8" in o and "9" in o: winner = "o"
    elif "1" in o and "4" in o and "7" in o: winner = "o"
    elif "2" in o and "5" in o and "8" in o: winner = "o"
    elif "3" in o and "6" in o and "9" in o: winner = "o"
    elif "1" in o and "5" in o and "9" in o: winner = "o"
    elif "3" in o and "5" in o and "7" in o: winner = "o"

def win(window, background):
    global winner, x, o, finished
    if not winner == "":
        win_label = main_font.render(f'Winner {winner.capitalize()}', True, (255,0,0))
        window.blit(background, (0,0))
        window.blit(win_label, (200 - win_label.get_width()/2, 200 - win_label.get_height()))
        finished = True
    elif len(x) + len(o) == 9 and winner == "":
        draw_label = main_font.render("DRAW", True, (255, 0, 0))
        window.blit(background, (0, 0))
        window.blit(draw_label, (200 - draw_label.get_width() / 2, 200 - draw_label.get_height()))
        finished = True


pygame.display.update()


run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            clicked(position)
            check()
            win(WIN, BG1)
            pygame.display.update()
