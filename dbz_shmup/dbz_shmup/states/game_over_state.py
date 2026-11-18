"""Ecran de defaite (minimal pour l'etape 1)."""
import pygame

import settings
from states.base_state import BaseState


class GameOverState(BaseState):
    def on_enter(self, score: int = 0, **kwargs) -> None:
        self.score = score
        self.big = pygame.font.Font(None, 64)
        self.font = pygame.font.Font(None, 30)

    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.manager.change("menu")

    def draw(self, screen) -> None:
        screen.fill(settings.COLOR_BG)
        t = self.big.render("GAME OVER", True, (230, 70, 70))
        s = self.font.render(f"Score : {self.score}", True, settings.COLOR_WHITE)
        h = self.font.render("ENTREE pour revenir au menu", True, (160, 160, 190))
        cx = settings.SCREEN_WIDTH // 2
        screen.blit(t, t.get_rect(center=(cx, 280)))
        screen.blit(s, s.get_rect(center=(cx, 350)))
        screen.blit(h, h.get_rect(center=(cx, 420)))
