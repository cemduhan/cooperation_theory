import random
from Players.Player import Player
from RoundState import PlayerAction

class RandomPlayer(Player):
    opponent_last_play = PlayerAction.COOPERATE
    name = "Random Player"
    behaviour = "Player randomly"
    def Play(self):
        if random.randint(0, 10) >= 5:
            return PlayerAction.CHEAT
        else:
            return PlayerAction.COOPERATE

