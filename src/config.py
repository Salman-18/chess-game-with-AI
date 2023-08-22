import pygame
from sound import Sound
from theme import Theme
class Config:
    def __init__(self):
        self._theeme = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        # font
        pass
    
    def change_theme(self):
        pass

    def _add_themes(self):
        pass 