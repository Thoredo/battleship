import pygame


class GameDifficulty:
    def __init__(self, display, game_state_manager, screen_width):
        self.display = display
        self.game_state_manager = game_state_manager
        self.screen_width = screen_width

        # load button images
        self.solo_easy_button = pygame.image.load("img/solo_easy.png")
        self.solo_hard_button = pygame.image.load("img/solo_hard.png")
        self.local_duel_button = pygame.image.load("img/local_duel.png")
        self.back_button = pygame.image.load("img/back.png")

        # Button positions
        self.solo_easy_button_rect = self.solo_easy_button.get_rect(
            center=(self.screen_width // 2, 190)
        )
        self.solo_hard_button_rect = self.solo_hard_button.get_rect(
            center=(self.screen_width // 2, 320)
        )
        self.local_duel_button_rect = self.local_duel_button.get_rect(
            center=(self.screen_width // 2, 450)
        )
        self.back_button_rect = self.back_button.get_rect(
            center=(self.screen_width // 2, 580)
        )

    def run(self):
        self.display.blit(self.solo_easy_button, self.solo_easy_button_rect.topleft)
        self.display.blit(self.solo_hard_button, self.solo_hard_button_rect.topleft)
        self.display.blit(self.local_duel_button, self.local_duel_button_rect.topleft)
        self.display.blit(self.back_button, self.back_button_rect.topleft)

        if pygame.mouse.get_pressed()[0]:
            if self.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.game_state_manager.set_state("main menu")
