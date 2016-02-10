﻿import pygame

window_height = 1000
window_width = 1000
gamename = "test"
tickspersec = 10
fps = 60
UnlimitedFPS = False #Turning this to true makes you render as many frames per second as possible

tickspeed = 1000/tickspersec
framespeed = 1000/fps

nextticktime = pygame.time.get_ticks()
nextrendertime = pygame.time.get_ticks()

fpsTime = pygame.time.Clock()
GameScreen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(gamename)