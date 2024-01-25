import os
import pygame as py
import sys
import math
import time
import random
from urllib.request import urlopen

start2button = False

py.init()
screenResolution = py.display.Info()
py.display.set_mode((screenResolution.current_w, screenResolution.current_h))
clock = py.time.Clock()
running = True
textGood = False

SCREEN_WIDTH = 1536
SCREEN_HIGHT = 864

titleList = []

repeat = True
offset = 0
while repeat:
    url = "https://realpython.github.io/fake-jobs/"
    page = urlopen(url)
    html = page.read()
    html = html.decode("utf-8")
    print(html)
    if html.find('<h2 class="title is-5">', offset) + len('<h2 class="title is-5">') != "":
        titleStart = html.find('<h2 class="title is-5">', offset) + len('<h2 class="title is-5">')
        titleEnd = html.find('</h2>', offset)
        print(titleStart)
        print(titleEnd)
        title = html[titleStart:titleEnd]
        titleList.append(title)
        html.replace(title, "")
        print(title)
        offset += titleEnd
        if offset >= len(html):
            repeat = False
            print(titleList)


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
bg = py.image.load("images\Background2.png").convert()
Start1 = py.image.load("images\Start1.png")
start1 = py.transform.scale(Start1, (310, 140))
Start2 = py.image.load("images\Start2.png")
start2 = py.transform.scale(Start2, (310, 140))

#background width
bg = py.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HIGHT))
bg_width = bg.get_width()

#moving background
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

def text(string): #we'll see
#offsets
    a = 0
    b = 3

    for x in string:
        print(x)
        break

def buttons(x, y, xLen, yLen):
    button = py.Rect(x, y, xLen, yLen)
    return button

def menu():
    if start2button == True:
        startbutton = screen.blit(start2, (SCREEN_WIDTH/2 - 155, SCREEN_HIGHT/2 - 70))
    else:
        startbutton = screen.blit(start1, (SCREEN_WIDTH/2 - 155, SCREEN_HIGHT/2 - 70))

    return(startbutton)

while running == True:
    mouse = py.mouse.get_pos()
    clock.tick(60)
#blit moving screen
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    scroll -= 0.5

    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
            # ----- blit only after this point -----
    menu()

    for event in py.event.get():
        if event.type == py.QUIT: #quit game via X button
            py.quit()
            sys.exit()
            print("Quitting...")
        elif event.type == py.KEYDOWN: #quit via esc key
            if event.key == py.K_ESCAPE:
                py.quit()
                sys.exit()
                print("Quitting...")
        elif event.type == py.MOUSEBUTTONDOWN: #mouse pressed
            if menu().collidepoint(event.pos):
                textGood = False
                games = []
                start2button = True
                totalNum = -1
                print("working!")



        elif event.type == py.MOUSEBUTTONUP: #mouse released
            start2button = False

    py.display.update()