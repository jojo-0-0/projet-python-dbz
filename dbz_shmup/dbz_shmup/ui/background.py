"""Fond d'etoiles defilant (affichage seul)."""
import random

import pygame

import settings


class Starfield:
    def __init__(self, count: int = 70):
        self.stars = [[random.uniform(0, settings.SCREEN_WIDTH),
                       random.uniform(0, settings.SCREEN_HEIGHT),
                       random.uniform(30, 140)] for _ in range(count)]

    def update(self, dt: float) -> None:
        for s in self.stars:
            s[1] += s[2] * dt
            if s[1] > settings.SCREEN_HEIGHT:
                s[0], s[1] = random.uniform(0, settings.SCREEN_WIDTH), 0

    def draw(self, screen) -> None:
        for x, y, v in self.stars:
            c = int(80 + v)
            pygame.draw.circle(screen, (c, c, c), (int(x), int(y)), 1 if v < 90 else 2)
