import numpy as np
from DotsGame.Events.Event import Event


class GameField:
    dotType = int
    dots = {}

    dotAddedEvent = Event()

    def __init__(self, dot_type):
        self.dotType = dot_type

    def add_new_dot(self, position):
        if(position in self.dots.keys()):
            return
        newDot = self.dotType()
        self.dots[position] = newDot
        print(position)
        self.dotAddedEvent.invoke(position)

    def get_dots_positions(self):
        return self.dots.keys()

    def is_contains_dot(self, position):
        return position in self.dots.keys()