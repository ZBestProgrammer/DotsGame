from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from DotsGame.Injections import *
from DotsGame.GameField import *

#cicleFinder.cycleAddedEvent.add_listener()

def showCicles():
    cycles = cicleFinder.get_cicles()
    cycles = list(map(list, map(list, cycles)))
    
    return cycles

def main(request):
    print("main")
    return render(request, 'index.html')

def test(request):
    print("test")
    if request.method == 'POST':
        position = request.POST.get('position')
        position = tuple(map(int, position.split(',')))
        gameField.add_new_dot(position)
        cycles = showCicles()
        dotsList = list(gameField.get_dots_positions())        
        color = 'blue'
        data = {
            'cycles': cycles,
            'dots': dotsList,
            'color': color
        }
        return JsonResponse(data=data)



    return HttpResponseRedirect('/')




