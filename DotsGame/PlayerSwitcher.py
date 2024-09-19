from DotsGame import CicleFinder
from DotsGame.GameField import GameField
from DotsGame.Events.Event import Event

class Input:
    move_made_event = None
    
    def __init__(self) -> None:
        self.move_made_event = Event()

    def make_move(self, move):
        self.move_made_event.invoke(move)

class Player:
    input = None
    gameField = None
    cycleFinder = None
    dots = []
    cycles = []
    dots_in_cycles = []

    color = ""

    def __init__(self, input:Input, gameField:GameField, cycleFinder:CicleFinder, color:str) -> None:
        self.input = input
        self.gameField = gameField
        self.cycleFinder = cycleFinder
        self.color = color
    
    def add_move_input_lisener(self, func):
        self.input.move_made_event.add_listener(lambda x : func(self, x))
    
    def move(self, move):
        if(self.gameField.add_new_dot(move)):
            self.cycles, self.dots_in_cycles = self.cycleFinder.find_filtred_cycles(move)
            self.dots = self.cycleFinder.G.nodes

        


class PlayerSwitcher:
    game_field = None
    players = []
    currentPlayerIndex = 0

    def __init__(self, gameField:GameField, players:list) -> None:
        self.game_field = gameField
        self.players = players
        for player in players:
            player.add_move_input_lisener(self.make_move)

    def get_current_player(self) -> Input:
        return self.players[self.currentPlayerIndex]
        
    def make_move(self, player, move) -> bool:
        print("Player:", self.currentPlayerIndex, self.get_current_player())
        if(player == self.get_current_player()):
            print("P", self.currentPlayerIndex)
            player.move(move)
    
    def switch_player(self):
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)

