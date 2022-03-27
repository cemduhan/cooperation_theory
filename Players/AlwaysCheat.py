from RoundState import PlayerAction
from Player import Player

class AlwaysCheat(Player):
    opponent_last_play = PlayerAction.CHEAT
    score = 0
    name = "Cooperative Player"
    behaviour = "Always Cheats"
    def Play(self):
        return PlayerAction.CHEAT