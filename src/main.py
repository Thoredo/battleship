import pygame
from core.game_state_manager import GameStateManager
from states.game_window import GameWindow
from states.main_menu import MainMenu

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.background_image = pygame.image.load("img/background.png")
        self.screen.blit(self.background_image, (0, 0))

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(
            self.screen, self.game_state_manager, SCREEN_WIDTH, self.close_game
        )
        self.game_window = GameWindow(self.screen, self.game_state_manager)

        self.states = {"main menu": self.main_menu, "game window": self.game_window}

    def close_game(self):
        self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()

            self.states[self.game_state_manager.get_state()].run()

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.quit()
