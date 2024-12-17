import pygame
from core.game_state_manager import GameStateManager
from states.game_window import GameWindow
from states.main_menu import MainMenu
from states.game_difficulty import GameDifficulty

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.game_state_manager = GameStateManager("main menu", self.screen)
        self.main_menu = MainMenu(
            self.screen, self.game_state_manager, SCREEN_WIDTH, self.close_game
        )
        self.game_window = GameWindow(self.screen, self.game_state_manager)
        self.game_difficulty = GameDifficulty(
            self.screen, self.game_state_manager, SCREEN_WIDTH
        )

        self.states = {
            "main menu": self.main_menu,
            "game window": self.game_window,
            "game difficulty": self.game_difficulty,
        }

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
