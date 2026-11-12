import pygame
from settings import LARGEUR, HAUTEUR, ORANGE, JAUNE

class PlayerData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.score = 0
        self.hp = 100
        self.max_hp = 100
        self.ki = 50
        self.max_ki = 100
        self.senzu_count = 1
        self.unlocked_weapons = ["KIKOHA"]


class Goku(pygame.sprite.Sprite):
    def __init__(self):
        # Apparence de Goku (en attendant l'image)
        self.image = pygame.Surface((50, 50))
        self.image.fill(ORANGE)

        self.rect = self.image.get_rect(center=(LARGEUR // 2, HAUTEUR - 80))
        self.vitesse = 6
        self.dernier_tir = 0
        self.delai_tir = 250  # ( Temps en ms entre deux tirs a tester )
    def uptade (self):
    def tirer (self) :
        






class Kikoha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Apparence du tir 
        self.image = pygame.Surface((8, 20))
        self.image.fill(JAUNE)
        self.rect = self.image.get_rect(center=(x, y))
        self.vitesse = -10  # Négatif car il monte vers le haut de l'écran

    def update(self):
        self.rect.y += self.vitesse
        # Supprime le tir s'il sort de l'écran en haut
        if self.rect.bottom < 0:
            self.kill()