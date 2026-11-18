"""Systeme d'armement (Strategy Pattern).

Le Player possede un `weapon` (composition) et l'appelle via try_fire().
Il ne sait jamais QUEL type d'arme il tient : pour l'etape 2, on cree
SpreadShot / PiercingLaser / AoEBomb heritant de Weapon et on les assigne
avec player.set_weapon(...). Aucune modification de ShmupState necessaire.
"""
from abc import ABC, abstractmethod

from entities.projectile import Projectile


class Weapon(ABC):
    def __init__(self, cooldown: float, base_damage: float):
        self.cooldown = cooldown          # secondes entre deux tirs
        self.base_damage = base_damage
        self._timer = 0.0

    def update(self, dt: float) -> None:
        self._timer = max(0.0, self._timer - dt)

    def try_fire(self, owner, group) -> bool:
        """Tire si le timer est ecoule ; ajoute les projectiles a `group`."""
        if self._timer > 0:
            return False
        self._timer = self.cooldown
        for proj in self.create_projectiles(owner):
            group.add(proj)
        return True

    @abstractmethod
    def create_projectiles(self, owner) -> list[Projectile]:
        """Fabrique les projectiles (Factory Method) - a implementer."""


class BasicKikoha(Weapon):
    """Tir droit standard, collision 1 contre 1."""

    SPEED = 650.0

    def create_projectiles(self, owner) -> list[Projectile]:
        damage = self.base_damage * owner.attack   # multiplicateur de stats
        return [Projectile(pos=owner.rect.midtop,
                           velocity=(0, -self.SPEED),
                           damage=damage)]
