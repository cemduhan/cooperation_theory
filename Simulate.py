import json
from RoundState import PlayerAction
from GameManager import GameManager
from Players.AlwaysCooperate import AlwaysCooperate
from Players.AlwaysCheat import AlwaysCheat
from Players.Grudjer import Grudjer
from Players.CopyCat import CopyCat
from Players.Forgiver import Forgiver
from Players.RandomPlayer import RandomPlayer
from Players.HumanPlayer import HumanPlayer

def SimulateGames(data):
    manager = GameManager()
    manager.SetGameValues(data["rounds"], data["win"],data["lose"])

    manager.SetPlayers(AlwaysCooperate,AlwaysCooperate)
    manager.Simulate()
    manager.Results()

    manager.SetPlayers(AlwaysCooperate,AlwaysCheat)
    manager.Simulate()
    manager.Results()

    manager.SetPlayers(AlwaysCheat,CopyCat)
    manager.Simulate()
    manager.Results()

    manager.SetPlayers(RandomPlayer,Forgiver)
    manager.Simulate()
    manager.Results()

    manager.SetPlayers(Grudjer,AlwaysCheat)
    manager.Simulate()
    manager.Results()

    manager.SetPlayers(Grudjer,HumanPlayer)
    manager.Simulate()
    manager.Results()

if __name__ == "__main__":
    with open('data.json') as json_file:
        data = json.load(json_file)
        SimulateGames(data)