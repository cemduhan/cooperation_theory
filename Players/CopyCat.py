from Players.Player import Player
from RoundState import PlayerAction

class CopyCat(Player):
    opponent_last_play = PlayerAction.COOPERATE
    score = 0
    name = "CopyCay Player"
    behaviour = "Copies Opponents Actions"
    def Play(self):
        return self.opponent_last_play