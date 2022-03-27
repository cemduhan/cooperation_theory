from RoundState import PlayerAction
from Player import Player

class AlwaysCooperate(Player):
    opponent_last_play = PlayerAction.COOPERATE
    score = 0
    name = "Cooperative Player"
    behaviour = "Always Cooperates"
    def Play(self):
        return PlayerAction.COOPERATE