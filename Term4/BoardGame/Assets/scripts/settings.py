import pygame as pg
import random
import os

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
WIDTH = 1920
HEIGHT = 1080
TITLE = "Title"

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


def draw_text(screen, text, size, x, y, color, font = 'rockwell'):
    font_name = pg.font.match_font(font)
    font = pg.font.Font(font_name, size)
    text_sprite = font.render(text, False, color)
    text_rect = text_sprite.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_sprite, text_rect)