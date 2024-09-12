from Dot import Dot

class GameField:
    dots = {}
    
    def addNewDot(self, position):
        newDot = Dot()
        self.dots[position] = newDot 

    def getDots(self):
        return self.dots