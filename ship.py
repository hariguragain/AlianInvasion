#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:57:27 2019

@author: hariguragain
"""

import pygame
class Ship():
    
    
    def __init__(self, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen
        # Load the ship image, and get its rect.
        self.image = pygame.image.load('../ehmatthes-pcc-f555082/chapter_12/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        