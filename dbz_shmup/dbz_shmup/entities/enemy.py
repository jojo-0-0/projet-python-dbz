"""Ennemis : update_movement() est le point de polymorphisme."""
from abc import ABC, abstractmethod

import pygame

import settings
from entities.entity import Entity


class Enemy(Entity, ABC):
    def __init__(self, pos, size, color, speed, max_hp,
                 score: int = 10, contact_damage: int = 15):
        super().__init__(pos, size, color, speed=speed, max_hp=max_hp)
        self.score = score
        self.contact_damage = contact_damage

    @abstractmethod
    def update_movement(self, dt: float) -> None:
        """Modifie self.pos. Surcharge par chaque type d'ennemi."""

    def update(self, dt: float) -> None:
        self.update_movement(dt)
        self.sync_rect()
        if self.rect.top > settings.SCREEN_HEIGHT + settings.OFFSCREEN_MARGIN:
            self.kill()


class LinearEnemy(Enemy):
    """Soldat de Freezer : descente en ligne droite."""

    def __init__(self, pos):
        super().__init__(pos, (34, 34), settings.COLOR_FRIEZA_SOLDIER,
                         speed=120, max_hp=20, score=10, contact_damage=15)

    def draw_shape(self, surf) -> None:
        r = surf.get_rect()
        pygame.draw.polygon(surf, self.color,
                            [(r.left, r.top), (r.right, r.top), (r.centerx, r.bottom)])

    def update_movement(self, dt: float) -> None:
        self.pos.y += self.speed * dt
