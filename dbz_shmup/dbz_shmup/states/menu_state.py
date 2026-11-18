"""Menu : choix du personnage (Goku / Vegeta)."""
import pygame

import settings
from entities.player import PROFILES
from states.base_state import BaseState


class MenuState(BaseState):
    def __init__(self, manager):
        super().__init__(manager)
        self.index = 0
        self.title_font = pygame.font.Font(None, 54)
        self.font = pygame.font.Font(None, 28)

    def handle_event(self, event) -> None:
        if event.type != pygame.KEYDOWN:
            return
        if event.key in (pygame.K_LEFT, pygame.K_q, pygame.K_a):
            self.index = (self.index - 1) % len(PROFILES)
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.index = (self.index + 1) % len(PROFILES)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            # Transfert du profil choisi vers ShmupState.on_enter(profile=...)
            self.manager.change("shmup", profile=PROFILES[self.index])
        elif event.key == pygame.K_ESCAPE:
            self.manager.quit()

    def draw(self, screen) -> None:
        screen.fill(settings.COLOR_BG)
        title = self.title_font.render("CHOISIS TON GUERRIER", True, settings.COLOR_WHITE)
        screen.blit(title, title.get_rect(center=(settings.SCREEN_WIDTH // 2, 100)))

        card_w, card_h = 190, 300
        for i, p in enumerate(PROFILES):
            x = 30 + i * (card_w + 40)
            card = pygame.Rect(x, 200, card_w, card_h)
            pygame.draw.rect(screen, (25, 28, 55), card, border_radius=10)
            pygame.draw.rect(screen, p.color, pygame.Rect(card.centerx - 25, 230, 50, 70), border_radius=8)
            border = settings.COLOR_WHITE if i == self.index else (60, 60, 90)
            pygame.draw.rect(screen, border, card, 3 if i == self.index else 1, border_radius=10)
            lines = [p.name, f"PV : {p.max_hp}", f"Attaque : x{p.attack}",
                     f"Cadence : {1 / p.weapon_factory().cooldown:.1f}/s", f"Special : {p.special_name}"]
            for j, line in enumerate(lines):
                surf = self.font.render(line, True, settings.COLOR_WHITE if j else p.color)
                screen.blit(surf, surf.get_rect(center=(card.centerx, 340 + j * 32)))

        hint = self.font.render("< > choisir   |   ENTREE valider", True, (160, 160, 190))
        screen.blit(hint, hint.get_rect(center=(settings.SCREEN_WIDTH // 2, 600)))
