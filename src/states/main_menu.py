import pygame


class MainMenu:
    def __init__(self, display, game_state_manager, screen_width, close_game):
        self.display = display
        self.game_state_manager = game_state_manager
        self.screen_width = screen_width
        self.close_game = close_game

        # Load button images
        self.play_button = pygame.image.load("img/play.png")
        self.options_button = pygame.image.load("img/options.png")
        self.exit_button = pygame.image.load("img/exit.png")

        # Button positions
        self.play_button_rect = self.play_button.get_rect(
            center=(self.screen_width // 2, 220)
        )
        self.options_button_rect = self.options_button.get_rect(
            center=(self.screen_width // 2, 350)
        )
        self.exit_button_rect = self.exit_button.get_rect(
            center=(self.screen_width // 2, 480)
        )

    def run(self):
        self.display.blit(self.play_button, self.play_button_rect.topleft)
        self.display.blit(self.options_button, self.options_button_rect.topleft)
        self.display.blit(self.exit_button, self.exit_button_rect.topleft)

        if pygame.mouse.get_pressed()[0]:
            if self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.close_game()
            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.game_state_manager.set_state("game difficulty")
