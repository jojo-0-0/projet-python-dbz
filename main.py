import pygame
import sys
from settings import LARGEUR, HAUTEUR, FPS, NOIR
from player import Goku

# Initialisation de Pygame
pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Titre jeux")
horloge = pygame.time.Clock()

pygame.quit()
sys.exit()
test = Goku()