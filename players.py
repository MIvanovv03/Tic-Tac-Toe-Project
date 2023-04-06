import random
import math

class Players:
    def __init__(self,player_letter):
        self.player_letter = player_letter
    def make_move(self,game):
        pass
class ComputerPlayer(Players):
    def __init__(self, player_letter):
        super().__init__(player_letter)
    def make_move(self,game):
        square = random.choice(game.available_moves())
        return square
class HumanPlayer(Players):
    def __init__(self, player_letter):
        super().__init__(player_letter)
    def make_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.player_letter + '\'𝕤 𝕥𝕦𝕣𝕟. 𝕄𝕒𝕜𝕖 𝕒 𝕞𝕠𝕧𝕖 𝕗𝕣𝕠𝕞 𝟘-𝟠: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    return ValueError
                valid_square = True
            except ValueError:
                print('𝕋𝕙𝕒𝕥 𝕚𝕤 𝕟𝕠𝕥 𝕒𝕧𝕒𝕚𝕝𝕒𝕓𝕝𝕖 𝕞𝕠𝕧𝕖! ')
                exit()
        return val


    