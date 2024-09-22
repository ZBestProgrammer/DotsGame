from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from DotsGame.Injections import *
from DotsGame.GameField import *

#cicleFinder.cycleAddedEvent.add_listener()

def show():
    datas = []
    for player in players:
        cycles = list(map(list, map(list, player.cycles)))
        dots_in_cycle = player.dots_in_cycles
        datas.append({
            'cycles': cycles,
            'dots': list(player.dots),
            'color': player.color,
            'dots_in_cycle': []
        })
    return datas

def main(request):
    return render(request, 'index.html')

def test(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        position = tuple(map(int, position.split(',')))
        uiInput.make_move(position)
        datas = show()
        return JsonResponse(data={'data': datas})
    return HttpResponseRedirect('/')




