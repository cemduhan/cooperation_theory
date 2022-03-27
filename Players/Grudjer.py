from Players.Player import Player
from RoundState import PlayerAction

class Grudjer(Player):
    opponent_last_play = PlayerAction.COOPERATE
    opponent_cheat = False
    name = "Grudjer Player"
    behaviour = "Cooperates until opponents cheats then cheats all the time"
    def Play(self):
        if self.opponent_last_play == PlayerAction.CHEAT:
            self.opponent_cheat = True
        if self.opponent_cheat:
            return PlayerAction.CHEAT
        else:
            return PlayerAction.COOPERATE

