from DotsGame import CicleFinder
from DotsGame.GameField import GameField
from DotsGame.Events.Event import Event
import pandas as pd


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
    count_of_win_dots = 0

    color = ""

    def __init__(self, input: Input, gameField: GameField, cycleFinder: CicleFinder, color: str) -> None:
        self.input = input
        self.gameField = gameField
        self.cycleFinder = cycleFinder
        self.color = color

    def add_move_input_lisener(self, func):
        self.input.move_made_event.add_listener(lambda x: func(self, x))

    def move(self, move, players):
        if self.gameField.add_new_dot(move):
            cycles_dots_in = self.cycleFinder.find_filtred_cycles(move)
            #self.cycles, self.dots_in_cycles = self.filtre_cycle(cycles_dots_in)
            self.dots = list(self.cycleFinder.G.nodes)
            self.count_of_win_dots = 0 #есть чужие точки
            self.cycles = []
            self.dots_in_cycles = []
            for cycle_dots in cycles_dots_in:
                count_dots_in_current_cycle = 0
                for player in players:
                    if player != self:
                        count_dots_in_current_cycle += player.eat_dots(cycle_dots[1])
                if count_dots_in_current_cycle > 0:
                    self.cycles.append(cycle_dots[0])
                    self.dots_in_cycles += cycle_dots[1]
                    self.count_of_win_dots += count_dots_in_current_cycle
            for dot in self.dots_in_cycles:
                self.gameField.add_new_dot(dot)
            print(self.color, "win dots:", self.count_of_win_dots)
            return True
        return False

    def eat_dots(self, dots_in_ather_cycles):
        s1 = pd.Series(dots_in_ather_cycles)
        s2 = pd.Series(self.dots)
        intersection = list(s1[s1.isin(s2)])
        for x in intersection:
            self.cycleFinder.remove(x)
        return len(intersection)


class PlayerSwitcher:
    players = []
    currentPlayerIndex = 0

    def __init__(self, players: list) -> None:
        self.players = players
        for player in players:
            player.add_move_input_lisener(self.make_move)

    def get_current_player(self) -> Input:
        return self.players[self.currentPlayerIndex]

    def make_move(self, player, move) -> bool:
        if player == self.get_current_player():
            if player.move(move, self.players):
                self.switch_player()

    def switch_player(self):
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)
