"""Projectiles (le deplacement est un vecteur vitesse : trajectoires libres)."""
from pygame.math import Vector2

import settings
from entities.entity import Entity


class Projectile(Entity):
    def __init__(self, pos, velocity, damage: float,
                 size=(8, 20), color=settings.COLOR_KIKOHA):
        super().__init__(pos, size, color, max_hp=1)
        self.velocity = Vector2(velocity)   # px / s
        self.damage = damage

    def draw_shape(self, surf) -> None:
        import pygame
        pygame.draw.ellipse(surf, self.color, surf.get_rect())

    def on_hit(self, target) -> None:
        """Hook polymorphe appele a chaque impact.

        Par defaut le projectile disparait (1 contre 1). Etape 2 : le
        PiercingLaser surchargera cette methode pour ne PAS se detruire,
        et l'AoEBomb pour instancier une ExplosionZone.
        """
        self.kill()

    def update(self, dt: float) -> None:
        self.pos += self.velocity * dt
        self.sync_rect()
        m = settings.OFFSCREEN_MARGIN
        if (self.rect.bottom < -m or self.rect.top > settings.SCREEN_HEIGHT + m
                or self.rect.right < -m or self.rect.left > settings.SCREEN_WIDTH + m):
            self.kill()
