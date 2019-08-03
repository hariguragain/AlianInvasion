#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 22:45:33 2019

@author: hariguragain
"""

import sys
import pygame


def check_events():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    
def update_screen(ai_settings, screen, ship):
    
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #Make the most recently drawn screen visible.
    pygame.display.flip()