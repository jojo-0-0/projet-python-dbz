"""Machine a etats globale (State Pattern).

Le StateManager ne connait QUE l'interface BaseState : ajouter un nouvel etat
(TurnBasedBossState a l'etape 4) = un register() de plus dans main.py.
"""
from states.base_state import BaseState


class StateManager:
    def __init__(self):
        self._states: dict[str, BaseState] = {}
        self.current: BaseState | None = None
        self.running = True

    def register(self, name: str, state: BaseState) -> None:
        self._states[name] = state

    def change(self, name: str, **kwargs) -> None:
        """Bascule vers l'etat `name`.

        Les **kwargs sont transmis a on_enter() : c'est le canal de transfert
        de donnees entre etats (ex. le Player de la Phase 1 -> Phase 2).
        """
        if self.current is not None:
            self.current.on_exit()
        self.current = self._states[name]
        self.current.on_enter(**kwargs)

    def quit(self) -> None:
        self.running = False

    # --- delegation vers l'etat courant ---------------------------------
    def handle_event(self, event) -> None:
        self.current.handle_event(event)

    def update(self, dt: float) -> None:
        self.current.update(dt)

    def draw(self, screen) -> None:
        self.current.draw(screen)
