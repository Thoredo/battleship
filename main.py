import pygame

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
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.game_window = GameWindow(self.screen, self.game_state_manager)

        self.states = {"main menu": self.main_menu, "game window": self.game_window}

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.states[self.game_state_manager.get_state()].run()

            pygame.display.flip()
            self.clock.tick(FPS)


class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        # Load button images
        self.play_button = pygame.image.load("img/play.png")
        self.options_button = pygame.image.load("img/options.png")
        self.exit_button = pygame.image.load("img/exit.png")

        # Button positions
        self.play_button_rect = self.play_button.get_rect(
            center=(SCREEN_WIDTH // 2, 220)
        )
        self.options_button_rect = self.options_button.get_rect(
            center=(SCREEN_WIDTH // 2, 350)
        )
        self.exit_button_rect = self.exit_button.get_rect(
            center=(SCREEN_WIDTH // 2, 480)
        )

    def run(self):
        self.display.blit(self.play_button, self.play_button_rect.topleft)
        self.display.blit(self.options_button, self.options_button_rect.topleft)
        self.display.blit(self.exit_button, self.exit_button_rect.topleft)


class GameWindow:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self):
        self.display.fill("blue")  # Example background for the game window


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.quit()
