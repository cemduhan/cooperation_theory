import random
from Players.Player import Player
from RoundState import PlayerAction

class Forgiver(Player):
    opponent_last_play = PlayerAction.COOPERATE
    opponent_cheat = False
    name = "Forgiving  Player"
    behaviour = "Forgives cheating with %50 chance"
    def Play(self):
        if self.opponent_last_play == PlayerAction.CHEAT:
            self.opponent_cheat = True
        if random.randint(0, 10) >= 5:
            self.opponent_cheat = False
        
        if self.opponent_cheat:
            return PlayerAction.CHEAT
        else:
            return PlayerAction.COOPERATE

