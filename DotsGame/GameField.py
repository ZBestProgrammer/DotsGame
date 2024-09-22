import numpy as np
from DotsGame.Events.Event import Event


class GameField:
    dots = set()

    dotAddedEvent = None

    def __init__(self):
        self.dots = set()
        self.dotAddedEvent = Event()

    def add_new_dot(self, position):
        if position in self.dots:
            return False
        self.dots.add(position)
        print(position)
        self.dotAddedEvent.invoke(position)
        return True

    def get_dots_positions(self):
        return self.dots

    def is_contains_dot(self, position):
        return position in self.dots
