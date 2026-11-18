"""Joueur : un seul code, deux profils de donnees (Goku / Vegeta)."""
from dataclasses import dataclass
from typing import Callable

import pygame
from pygame.math import Vector2

import settings
from entities.entity import Entity
from weapons.weapon import BasicKikoha, Weapon


@dataclass(frozen=True)
class CharacterProfile:
    """Profil de personnage = donnees pures (pas de logique)."""
    name: str
    color: tuple
    max_hp: int
    speed: float
    attack: float                       # multiplicateur de degats
    weapon_factory: Callable[[], Weapon]
    special_name: str                   # branche a l'etape 2/3


GOKU = CharacterProfile(
    name="Son Goku", color=settings.COLOR_GOKU,
    max_hp=100, speed=300, attack=1.4,
    weapon_factory=lambda: BasicKikoha(cooldown=0.30, base_damage=10),
    special_name="Kamehameha",
)
VEGETA = CharacterProfile(
    name="Vegeta", color=settings.COLOR_VEGETA,
    max_hp=150, speed=280, attack=1.0,
    weapon_factory=lambda: BasicKikoha(cooldown=0.16, base_damage=10),
    special_name="Final Flash",
)
PROFILES = [GOKU, VEGETA]


class Player(Entity):
    def __init__(self, profile: CharacterProfile, pos):
        super().__init__(pos, (36, 48), profile.color,
                         speed=profile.speed, max_hp=profile.max_hp)
        self.profile = profile
        self.attack = profile.attack
        self.weapon: Weapon = profile.weapon_factory()
        self.direction = Vector2()
        # Donnees destinees a etre transferees vers la Phase 2 (etape 4)
        self.ki = 0
        self.senzu = 0

    def draw_shape(self, surf) -> None:
        r = surf.get_rect()
        pygame.draw.rect(surf, self.color, r, border_radius=6)
        pygame.draw.circle(surf, (255, 220, 180), (r.centerx, 12), 9)  # tete

    def set_weapon(self, weapon: Weapon) -> None:
        """Point d'entree de l'etape 2 : changer d'arme sans toucher au reste."""
        self.weapon = weapon

    def handle_input(self, keys) -> None:
        """Lit le clavier -> vecteur direction (ZQSD, WASD ou fleches)."""
        d = Vector2(
            (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]),
            (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]),
        )
        # Normalisation : evite la diagonale plus rapide (vitesse * 1.41)
        self.direction = d.normalize() if d.length_squared() > 0 else d

    def shoot(self, projectile_group) -> bool:
        return self.weapon.try_fire(self, projectile_group)

    def on_death(self) -> None:
        # Le joueur n'est PAS kill() : ShmupState detecte hp <= 0.
        # C'est ici que l'etape 3 branchera le Revive (Haricot Senzu).
        pass

    def update(self, dt: float) -> None:
        self.pos += self.direction * self.speed * dt
        # Garde le joueur dans l'ecran
        half_w, half_h = self.rect.w / 2, self.rect.h / 2
        self.pos.x = max(half_w, min(settings.SCREEN_WIDTH - half_w, self.pos.x))
        self.pos.y = max(half_h, min(settings.SCREEN_HEIGHT - half_h, self.pos.y))
        self.weapon.update(dt)
        self.sync_rect()
