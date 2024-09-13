from django.shortcuts import render

from DotsGame.Injections import *

#cicleFinder.cycleAddedEvent.add_listener()

def showCicles():
    cycles = cicleFinder.get_cicles()
    cycles = list(map(list, cycles))
    print("nodes", cicleFinder.G.nodes)
    print(cycles)

def main(request):
    print("main")
    return render(request, 'index.html')

def test(request):
    dots = [[1, 2], [3, 4], [5, 6]]
    print("test")
    if request.method == 'POST':
        position = request.POST.get('position')
        position = tuple(map(int, position.split(',')))
        gameField.add_new_dot(position)

        showCicles()

    return render(request, 'index.html')




