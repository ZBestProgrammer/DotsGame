from django.shortcuts import render

from Classes.GameField import GameField

# class Dot:
#     chain = []

# class GameField:
#     dots = {}
    
#     def addNewDot(self, position):
#         newDot = Dot()
#         self.dots[position] = newDot 

#     def getDots(self):
#         return self.dots

gameField = GameField()

def main(request):
    return render(request, 'index.html')

def test(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        gameField.addNewDot(position)
        print(gameField.getDots())

       
    return render(request, 'index.html')

