import pandas as pd
import networkx as nx

from DotsGame.Events.Event import Event


class CicleFinderDot:
    chain = []


def add_tuples(a, b):
    return tuple(v1 + v2 for v1, v2 in zip(a, b))


class CicleFinder:
    gameField = 0
    G = nx.Graph()
    cycles = []

    def __init__(self, game_field):
        self.gameField = game_field
        self.gameField.dotAddedEvent.add_listener(self.dot_added)

    def get_cicles(self):
        return self.cycles

    def dot_added(self, new_dot_position):
        print("Событие работает: " + str(new_dot_position))
        neighbours = self.find_neighbours(new_dot_position)

        self.G.add_node(new_dot_position)
        for n in neighbours:
            self.G.add_edge(new_dot_position, n)
        self.cycles = nx.minimum_cycle_basis(self.G)


    def find_neighbours(self, position):
        offsets = [
            [1,0],
            [0,-1],
            [-1, 0],
            [0, 1],
            [1,1],
            [1,-1],
            [-1,-1],
            [-1,1]
        ]

        positions = map(lambda x: add_tuples(position, x), offsets)
        s1 = pd.Series(positions)
        s2 = pd.Series(self.gameField.dots.keys())
        return list(s1[s1.isin(s2)])
