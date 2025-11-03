import pygame as pg
import random
import os
import pyautogui
import sys
from pygame.math import Vector2 as vec

# Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
darkRed = (82,10,13)
green = (0,255,0)
blue = (0,0,255)
mint = (142,232,132)
yellow = (245,245,5)
violet = (160, 0, 250)
pink = (255, 0, 255)
lilac = (230,215,255)
transparent = (0,0,0,0)

SWIDTH = 800
SHEIGHT = 1000
WIDTH , HEIGHT= pyautogui.size()
TITLE = "PewPew"

FPS = 60
tileCount = (16, 16)
TILE_SIZE = (WIDTH/tileCount[0],HEIGHT/tileCount[1])
tile_w = WIDTH/tileCount[0]
tile_h = HEIGHT/tileCount[1]

gameDir = os.path.dirname(__file__)
gameDir = gameDir.replace("\Assets\scripts", "")
assetsDir = os.path.join(gameDir,"Assets")
mapDir = os.path.join(assetsDir,"maps")
scriptsDir = os.path.join(assetsDir,"scripts")
classDir = os.path.join(scriptsDir,"classes")
soundsDir = os.path.join(assetsDir,"sounds")
spritesDir = os.path.join(assetsDir,"sprites")

PATHS ={"game":gameDir,
        "assets":os.path.join(gameDir,"assets"),
        "sprites":os.path.join(gameDir,"assets\sprites"),
        "maps":os.path.join(gameDir,"assets\maps"),
        "scripts":os.path.join(gameDir,"assets\scripts"),
        "player":os.path.join(spritesDir,"player"),
        "coffin":os.path.join(spritesDir,"monster\coffin"),
        "cactus":os.path.join(spritesDir,"monster\cactus"),
        "bullet":os.path.join(spritesDir,"bullet"),
        "other":os.path.join(spritesDir,"other")}


def draw_text(screen, text, size, x, y, color=black, font = 'rockwell'):
    font_name = pg.font.match_font(font)
    font = pg.font.Font(font_name, size)
    text_sprite = font.render(text, False, color)
    text_rect = text_sprite.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_sprite, text_rect)