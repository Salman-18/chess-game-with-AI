import pygame
from sound import Sound
from theme import Theme
import os
class Config:
    def __init__(self):
        self._theeme = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        # font
        self.move_sound = Sound(
            os.path.join("assets/sound/move.wav"))
        self.caputre_sound = Sound(
            os.path.join("assets/sound/capture.wav"))
    
    def change_theme(self):
        self.ixd += 1
        

    def _add_themes(self):
        pass 