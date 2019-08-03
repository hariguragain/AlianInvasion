#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:12:50 2019

@author: hariguragain
My first Game, based on the book Python Crash Course by Eric Mattis
"""
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make a ship
    ship = Ship(screen)
    #set the background color.
    #bg_color = (230,230,230)
    
    #start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()
