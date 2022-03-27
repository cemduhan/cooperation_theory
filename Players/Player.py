from RoundState import PlayerAction

class Player:
    opponent_last_play = PlayerAction.COOPERATE
    score = 0
    name = "Default Player"
    behaviour = "Always plays Cooperate"
    def Play(self):
        return PlayerAction.COOPERATE
    def SetResult(self, round_score, opponent_play):
        self.score = self.score + round_score
        self.opponent_last_play = opponent_play
    def Print(self):
        print("Player Name: " + self.name)
        print("Behaviour: " + self.behaviour)
        print("Score: " + str(self.score))