import pygame


class GameStateManager:
    def __init__(self, current_state, screen):
        self.current_state = current_state
        self.screen = screen
        self.background_image = pygame.image.load("img/background.png")
        self.screen.blit(self.background_image, (0, 0))

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.screen.blit(self.background_image, (0, 0))
        self.current_state = state
