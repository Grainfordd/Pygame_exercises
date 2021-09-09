

class GameStats:

    def __init__(self, settings):

        self.settings = settings
        self.game_active = True
        self.lifes = settings.lifes_limit

    def game_reset(self):
        self.lifes = settings.lifes_limit