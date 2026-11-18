"""Interface en jeu : lit les donnees du Player, ne modifie rien."""
import pygame

import settings


class Hud:
    def __init__(self):
        self.font = pygame.font.Font(None, 26)

    def draw(self, screen, player, score: int) -> None:
        bar = pygame.Rect(10, 10, 160, 14)
        pygame.draw.rect(screen, settings.COLOR_HP_BAR_BG, bar)
        ratio = max(0, player.hp) / player.max_hp
        fill = bar.copy()
        fill.width = int(bar.width * ratio)
        pygame.draw.rect(screen, settings.COLOR_HP_BAR, fill)
        pygame.draw.rect(screen, settings.COLOR_WHITE, bar, 1)
        screen.blit(self.font.render(player.profile.name, True, settings.COLOR_WHITE), (10, 28))
        txt = self.font.render(f"Score {score}", True, settings.COLOR_WHITE)
        screen.blit(txt, (settings.SCREEN_WIDTH - txt.get_width() - 10, 10))
