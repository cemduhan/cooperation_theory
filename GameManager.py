from RoundState import PlayerAction


class GameManager:
    PlayerOne = None
    PlayerTwo = None
    TurnCount = 0
    WinScore = 0
    CooperateScore = 0
    def SetPlayers(self, PlayerOne, PlayerTwo):
        self.PlayerOne = PlayerOne
        self.PlayerTwo = PlayerTwo
    def SetGameValues(self, TurnCount, WinScore, CooperateScore):
        self.TurnCount = TurnCount
        self.WinScore = WinScore
        self.CooperateScore = CooperateScore
    def Simulate(self):
        for i in range(self.TurnCount):
            PlayerOneRoundPlay = self.PlayerOne.Play()
            PlayerTwoRoundPlay = self.PlayerTwo.Play()
            if PlayerOneRoundPlay == PlayerTwoRoundPlay and PlayerOneRoundPlay == PlayerAction.COOPERATE:
                self.PlayerOne.SetResult(self.CooperateScore,PlayerTwoRoundPlay)
                self.PlayerTwo.SetResult(self.CooperateScore,PlayerOneRoundPlay)
            if PlayerOneRoundPlay == PlayerAction.COOPERATE and PlayerTwoRoundPlay == PlayerAction.CHEAT:
                self.PlayerOne.SetResult(0,PlayerTwoRoundPlay)
                self.PlayerTwo.SetResult(self.WinScore,PlayerOneRoundPlay)
            if PlayerOneRoundPlay == PlayerAction.CHEAT and PlayerTwoRoundPlay == PlayerAction.COOPERATE:
                self.PlayerOne.SetResult(self.WinScore,PlayerTwoRoundPlay)
                self.PlayerTwo.SetResult(0,PlayerOneRoundPlay)
            if PlayerOneRoundPlay == PlayerAction.CHEAT and PlayerTwoRoundPlay == PlayerAction.CHEAT:
                self.PlayerOne.SetResult(0,PlayerTwoRoundPlay)
                self.PlayerTwo.SetResult(0,PlayerOneRoundPlay)
        return 1
    def Results(self):
        self.PlayerOne.Print()
        self.PlayerTwo.Print()

    