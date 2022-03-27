import random
from RoundState import PlayerAction
from Player import Player

class HumanPlayer(Player):
    opponent_last_play = PlayerAction.COOPERATE
    name = "Human Player"
    behaviour = "Human Player"
    def Play(self):
        print("Please put an input : Cheat or Coop")
        player_input = input()
        if player_input == "Cheat":
            return PlayerAction.CHEAT
        else:
            return PlayerAction.COOPERATE



