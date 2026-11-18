"""Classe de base de toutes les entites a l'ecran."""
import os

import pygame
from pygame.math import Vector2

import settings


class Entity(pygame.sprite.Sprite):
    """Position (vecteur 2D), hitbox, vitesse et points de vie.

    Pour passer des formes geometriques aux sprites PNG, il suffit de
    surcharger `build_image()` dans une sous-classe (voir load_sprite).
    """

    hitbox_scale = 0.8  # hitbox legerement plus petite que l'image

    def __init__(self, pos, size, color, speed: float = 0.0, max_hp: int = 1):
        super().__init__()
        self.pos = Vector2(pos)          # position reelle (float), centre
        self.size = size
        self.color = color
        self.speed = speed               # pixels / seconde
        self.max_hp = max_hp
        self.hp = max_hp
        self.image = self.build_image()
        self.rect = self.image.get_rect(center=self.pos)
        self.hitbox = self.rect.copy()
        self.hitbox.size = (int(self.rect.w * self.hitbox_scale),
                            int(self.rect.h * self.hitbox_scale))
        self.sync_rect()

    # --- rendu : point d'extension vers les sprites ----------------------
    def build_image(self) -> pygame.Surface:
        surf = pygame.Surface(self.size, pygame.SRCALPHA)
        self.draw_shape(surf)
        return surf

    def draw_shape(self, surf: pygame.Surface) -> None:
        """Forme geometrique par defaut. A surcharger par entite."""
        pygame.draw.rect(surf, self.color, surf.get_rect(), border_radius=4)

    @staticmethod
    def load_sprite(filename: str, size) -> pygame.Surface | None:
        """Charge assets/sprites/<filename> ; renvoie None si absent.

        Usage futur dans une sous-classe :
            def build_image(self):
                return self.load_sprite("goku.png", self.size) or super().build_image()
        """
        path = os.path.join(settings.SPRITE_DIR, filename)
        if not os.path.exists(path):
            return None
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, size)

    # --- logique --------------------------------------------------------
    def sync_rect(self) -> None:
        """Synchronise rect/hitbox (entiers) avec pos (flottants)."""
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.hitbox.center = self.rect.center

    def take_damage(self, amount: float) -> None:
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.on_death()

    def on_death(self) -> None:
        self.kill()

    def update(self, dt: float) -> None:
        self.sync_rect()
