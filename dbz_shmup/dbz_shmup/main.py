"""Point d'entree. Cette boucle ne changera plus jusqu'a la fin du projet :
chaque etape ajoute des etats / armes / entites, pas de logique ici."""
import pygame

import settings
from core.state_manager import StateManager
from states.game_over_state import GameOverState
from states.menu_state import MenuState
from states.shmup_state import ShmupState


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()

    manager = StateManager()
    manager.register("menu", MenuState(manager))
    manager.register("shmup", ShmupState(manager))
    manager.register("game_over", GameOverState(manager))
    # Etape 4 : manager.register("boss", TurnBasedBossState(manager)) ...
    manager.change("menu")

    while manager.running:
        dt = min(clock.tick(settings.FPS) / 1000.0, 0.05)  # dt borne (anti-saut)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                manager.quit()
            else:
                manager.handle_event(event)
        manager.update(dt)
        manager.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
