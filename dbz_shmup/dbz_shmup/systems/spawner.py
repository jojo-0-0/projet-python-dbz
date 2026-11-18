"""Apparition des ennemis, pilotee par une table (type, poids)."""
import random

import settings
from entities.enemy import Enemy, LinearEnemy


class EnemySpawner:
    def __init__(self, interval: float = 1.1):
        self.interval = interval
        self._timer = interval
        # Etape 3 : spawner.register(SineWaveEnemy, 2) / (KamikazeEnemy, 1)
        self._table: list[tuple[type[Enemy], int]] = [(LinearEnemy, 1)]

    def register(self, enemy_cls: type[Enemy], weight: int = 1) -> None:
        self._table.append((enemy_cls, weight))

    def update(self, dt: float, group) -> None:
        self._timer -= dt
        if self._timer <= 0:
            self._timer = self.interval
            classes, weights = zip(*self._table)
            cls = random.choices(classes, weights=weights)[0]
            x = random.randint(30, settings.SCREEN_WIDTH - 30)
            group.add(cls((x, -30)))
