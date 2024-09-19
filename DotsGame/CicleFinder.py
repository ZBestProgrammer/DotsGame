import pandas as pd
import networkx as nx

from DotsGame.Events.Event import Event

import matplotlib.path as mpath



class CicleFinderDot:
    chain = []


def add_tuples(a, b):
    return tuple(v1 + v2 for v1, v2 in zip(a, b))

class CicleFinder:
    G = None

    def __init__(self):
        self.G = nx.Graph()


    def find_filtred_cycles(self, new_dot_position):
        cycles = self.find_cycles(new_dot_position)
        cycles = [x for x in cycles if len(x) > 3]
        cyclesF = []
        dots_in_cyclesF = []
        for cycle in cycles:
            dots_in_cycle = self.find_dots_in_cycle(cycle)
            if(len(dots_in_cycle) > 0):
                cyclesF.append(cycle)
                dots_in_cyclesF += dots_in_cycle
        return cyclesF, dots_in_cyclesF
    
    
    def find_bounding_box(self, cycle):
        x_coords = [point[0] for point in cycle]
        y_coords = [point[1] for point in cycle]
        
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)

        bounding_box = [(min_x, min_y), (max_x, max_y)]
        return bounding_box
    
    
    def find_dots_in_cycle(self, cycle):
        dots_in_cycle = []
        polygon = mpath.Path(cycle)
        bounding_box = self.find_bounding_box(cycle)
        x1 = bounding_box[0][0]
        x2 = bounding_box[1][0]
        y1 = bounding_box[0][1]
        y2 = bounding_box[1][1]

        for x in range(x1, x2):
            for y in range(y1, y2):
                point = (x, y)
                if polygon.contains_point(point) and point not in cycle:
                    dots_in_cycle.append(point)

        return dots_in_cycle
    

    def find_cycles(self, new_dot_position):
        print("Поиск циклов: " + str(new_dot_position))
        neighbours = self.find_neighbours(new_dot_position)

        self.G.add_node(new_dot_position)
        for n in neighbours:
            self.G.add_edge(new_dot_position, n)
        return nx.minimum_cycle_basis(self.G)


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
        s2 = pd.Series(list(self.G.nodes)) 
        return list(s1[s1.isin(s2)])
