"""Constantes globales du jeu (aucune logique ici)."""

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Namek Shmup - Etape 1"

# Marge (px) au-dela de l'ecran avant de detruire une entite hors champ
OFFSCREEN_MARGIN = 60

# Palette (formes geometriques en attendant les sprites)
COLOR_BG = (8, 10, 28)
COLOR_WHITE = (240, 240, 240)
COLOR_GOKU = (255, 140, 0)        # orange
COLOR_VEGETA = (50, 90, 220)      # bleu
COLOR_KIKOHA = (255, 230, 80)     # jaune
COLOR_FRIEZA_SOLDIER = (150, 60, 190)  # violet
COLOR_HP_BAR = (80, 220, 100)
COLOR_HP_BAR_BG = (70, 30, 30)

# Dossier des sprites (voir Entity.load_sprite)
SPRITE_DIR = "assets/sprites"
