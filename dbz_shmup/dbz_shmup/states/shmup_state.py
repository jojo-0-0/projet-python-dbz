"""Phase 1 : shoot 'em up vertical en temps reel."""
import pygame

import settings
from entities.player import Player
from states.base_state import BaseState
from systems.spawner import EnemySpawner
from ui.background import Starfield
from ui.hud import Hud


def hitbox_collide(a, b) -> bool:
    """Collision sur les hitbox (pas sur les rect d'affichage)."""
    return a.hitbox.colliderect(b.hitbox)


class ShmupState(BaseState):
    def on_enter(self, profile=None, **kwargs) -> None:
        self.player = Player(profile, (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 90))
        self.projectiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.spawner = EnemySpawner()
        self.background = Starfield()
        self.hud = Hud()
        self.score = 0

    # --- entrees ---------------------------------------------------------
    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.manager.change("menu")

    # --- logique ---------------------------------------------------------
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        if keys[pygame.K_SPACE]:
            self.player.shoot(self.projectiles)

        self.background.update(dt)
        self.player.update(dt)
        self.projectiles.update(dt)
        self.enemies.update(dt)
        self.spawner.update(dt, self.enemies)

        self._resolve_collisions()

        if self.player.hp <= 0:
            # Etape 3 : le Revive (Senzu) sera gere dans Player.on_death
            self.manager.change("game_over", score=self.score)

    def _resolve_collisions(self) -> None:
        # Projectiles -> ennemis. Le projectile decide lui-meme de son sort
        # via on_hit() (polymorphisme : normal, perforant, explosif...).
        for proj in list(self.projectiles):
            for enemy in pygame.sprite.spritecollide(proj, self.enemies, False, hitbox_collide):
                enemy.take_damage(proj.damage)
                if not enemy.alive():
                    self.score += enemy.score
                proj.on_hit(enemy)
                if not proj.alive():
                    break

        # Ennemis -> joueur (contact)
        for enemy in pygame.sprite.spritecollide(self.player, self.enemies, False, hitbox_collide):
            self.player.take_damage(enemy.contact_damage)
            enemy.kill()

    # --- affichage -------------------------------------------------------
    def draw(self, screen) -> None:
        screen.fill(settings.COLOR_BG)
        self.background.draw(screen)
        self.enemies.draw(screen)
        self.projectiles.draw(screen)
        screen.blit(self.player.image, self.player.rect)
        self.hud.draw(screen, self.player, self.score)
