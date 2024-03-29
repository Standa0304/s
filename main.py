import pygame
import sys
import os
import random
import math
import time
from pygame.locals import *
from pygame import mixer

pygame.init()

# Obrazovka

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bubble blast")
background = pygame.image.load('background.png').convert()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# music = mixer.music.load("background.wav")
# mixer.music.play(-1)
# Text
font = pygame.font.Font('Blackbird.ttf', 20)
over_font = pygame.font.Font('Blackbird.ttf', 70)
celkove_font = pygame.font.Font('Blackbird.ttf', 40)
menu_font = pygame.font.Font('Blackbird.ttf', 80)
start_font = pygame.font.Font('Blackbird.ttf', 25)
# Hráč
player = pygame.image.load('player.png')
playerX = 370
playerY = 536
p_changeX = 0

# Balonek
balon = []
balonX = []
balonY = []
b_changeX = []
b_changeY = []
pocet_balon = 6
for i in range(pocet_balon):
    balon.append(pygame.image.load('enemy.png'))
    balonX.append(random.randint(0, 736))
    balonY.append(0)
    b_changeX.append(2)
    b_changeY.append(2)

# Koule ;)
koule = pygame.image.load('koule.png')
kouleX = 0
kouleY = 536
k_changeY = 5
nabito = "ready"

# Skore
skore = 0


# Funkce
def player_move(x, y):
    screen.blit(player, (x, y))


def enemy(x, y, i):
    screen.blit(balon[i], (x, y))


def fire_koule(x, y):
    global nabito
    nabito = "fire"
    screen.blit(koule, (x, y))


def konec_hry_text(skore):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    celkove_skore_text = celkove_font.render("Celkove skore: " + str(skore), True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    screen.blit(celkove_skore_text, (300, 320))


def kolize_koule(balonX, balonY, kouleX, kouleY):
    vzdalenost = math.sqrt((math.pow(balonX - kouleX, 2)) + (math.pow(balonY - kouleY, 2)))
    if vzdalenost < 27:
        return True
    else:
        return False


def kolize_hrace(balonX, balonY, playerX, playerY):
    vzdalenost = math.sqrt((math.pow(balonX - playerX, 2)) + (math.pow(balonY - playerY, 2)))
    if vzdalenost < 40:
        return True
    else:
        return False


def vypis_skrore(x, y):
    skore_text = font.render("Skore: " + str(skore), True, (255, 255, 255))
    screen.blit(skore_text, (x, y))


# Smyčka
menu = True
running = True
napoveda_screen = False
obtiznost = False
while running:

    while menu:
        menuf = menu_font.render("Bubble blast", True, (153, 0, 153))
        bck = pygame.image.load("bg.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if mx > 350 and mx < 450 and my > 300 and my < 350:
                    menu = False
                    napoveda_screen = False
                    obtiznost = True
                if mx > 350 and mx < 450 and my > 380 and my < 430:
                    menu = False
                    napoveda_screen = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False

        screen.fill((255, 255, 255))
        screen.blit(bck, (0, 0))
        screen.blit(menuf, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 300, 100, 50), 3)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 380, 100, 50), 3)
        start = start_font.render("Start", True, (0, 0, 0))
        napoveda = start_font.render("help", True, (0, 0, 0))
        screen.blit(start, (375, 310))
        screen.blit(napoveda, (380, 390))
        pygame.display.update()

    while napoveda_screen:
        screen.fill((255, 255, 255))
        screen.blit(bck, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
                napoveda_screen = False
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if mx > 350 and mx < 450 and my > 500 and my < 550:
                    napoveda_screen = False
                    obtiznost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                    napoveda_screen = False

        a = start_font.render("Arrow vpravo - Pohyb do prava", True, (255, 255, 255))
        b = start_font.render("Arrow vlevo - Pohyb do leva", True, (255, 255, 255))
        c = start_font.render("Mezerník - Palba", True, (255, 255, 255))
        d = start_font.render("Escape - Vypnuti hry", True, (255, 255, 255))
        e = start_font.render("P - Pauza", True, (255, 255, 255))
        screen.blit(a, (250, 150))
        screen.blit(b, (250, 200))
        screen.blit(c, (250, 250))
        screen.blit(d, (250, 300))
        screen.blit(e, (250, 350))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 500, 100, 50), 3)
        zacatek = start_font.render("Start", True, (0, 0, 0))
        screen.blit(zacatek, (375, 510))
        pygame.display.update()

    while obtiznost:
        screen.fill((255, 255, 255))
        screen.blit(bck, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
                napoveda_screen = False
                obtiznost = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                    obtiznost = False
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if mx > 350 and mx < 450 and my > 250 and my < 300:
                    obtiznost = False
                    b_chanyplus = 1
                    b_chanyminus = -1
                    b_chanxplus = 1
                    b_chanxminus = -1
                    for i in range(pocet_balon):
                        b_changeX[i] = 1
                        b_changeY[i] = 1
                if mx > 350 and mx < 450 and my > 350 and my < 400:
                    obtiznost = False
                    b_chanyplus = 2
                    b_chanyminus = -2
                    b_chanxplus = 2
                    b_chanxminus = -2
                    for i in range(pocet_balon):
                        b_changeX[i] = 2
                        b_changeY[i] = 2
                if mx > 350 and mx < 450 and my > 450 and my < 500:
                    obtiznost = False
                    b_chanyplus = 3
                    b_chanyminus = -3
                    b_chanxplus = 3
                    b_chanxminus = -3
                    for i in range(pocet_balon):
                        b_changeX[i] = 3
                        b_changeY[i] = 3

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 250, 100, 50), 3)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 350, 100, 50), 3)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 450, 100, 50), 3)
        easy = start_font.render("Easy", True, (0, 0, 0))
        medium = start_font.render("Medium", True, (0, 0, 0))
        hard = start_font.render("Hard", True, (0, 0, 0))
        screen.blit(easy, (370, 260))
        screen.blit(medium, (362, 360))
        screen.blit(hard, (375, 460))
        pygame.display.update()

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Vstupy hráče
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_changeX = -2
            if event.key == pygame.K_RIGHT:
                p_changeX = 2
            if event.key == pygame.K_SPACE:
                if nabito == "ready":
                    shoot = mixer.Sound("strelba.wav")
                    shoot.play()
                    kouleX = playerX
                    fire_koule(kouleX, kouleY)

            if event.key == pygame.K_p:
                menu = True
            if event.key == pygame.K_r:
                skore = 0
                for i in range(pocet_balon):
                    balonX[i] = (random.randint(0, 736))
                    balonY[i] = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p_changeX = 0

    # Balon
    for i in range(pocet_balon):
        balonX[i] += b_changeX[i]
        balonY[i] += b_changeY[i]
        if balonX[i] >= 736:
            b_changeX[i] = b_chanxminus
        if balonX[i] <= 0:
            b_changeX[i] = b_chanxplus
        if balonY[i] >= 536:
            b_changeY[i] = b_chanyminus
        if balonY[i] <= 0:
            b_changeY[i] = b_chanyplus

    # Pohyb
    playerX += p_changeX
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

    # Strelba
    if kouleY <= 0:
        kouleY = 536
        nabito = "ready"
    if nabito == "fire":
        fire_koule(kouleX, kouleY)
        kouleY -= k_changeY

    # Kolize
    for i in range(pocet_balon):
        koule_kolize = kolize_koule(balonX[i], balonY[i], kouleX, kouleY)
        if koule_kolize:
            kolize_zvuk = mixer.Sound("boom.wav")
            kolize_zvuk.play()
            kouleY = 480
            nabito = "ready"
            skore += 1
            balonX[i] = random.randint(0, 735)
            balonY[i] = 0
        hrac_kolize = kolize_hrace(balonX[i], balonY[i], playerX, playerY)
        if hrac_kolize:
            for j in range(pocet_balon):
                balonY[j] = playerY
                balonX[j] = playerX
                balon[j].fill((0, 0, 0, 0))
            konec_hry_text(skore)
            nabito = "konec"

        enemy(balonX[i], balonY[i], i)

    # Volání funkcí
    player_move(playerX, playerY)
    vypis_skrore(10, 10)
    # Update obrazovky
    pygame.display.update()