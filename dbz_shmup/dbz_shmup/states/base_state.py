"""Interface commune a tous les etats du jeu."""


class BaseState:
    def __init__(self, manager):
        self.manager = manager

    def on_enter(self, **kwargs) -> None:
        """Appele a chaque entree dans l'etat (recoit les donnees transmises)."""

    def on_exit(self) -> None:
        """Appele quand on quitte l'etat."""

    def handle_event(self, event) -> None:
        """Evenements ponctuels (touche pressee, fermeture fenetre...)."""

    def update(self, dt: float) -> None:
        """Logique metier. dt = secondes ecoulees depuis la derniere frame."""

    def draw(self, screen) -> None:
        """Affichage uniquement : aucune logique de jeu ici."""
