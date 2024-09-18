from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from DotsGame.Injections import *
from DotsGame.GameField import *

#cicleFinder.cycleAddedEvent.add_listener()

def show():
    datas = []
    for player in players:
        print(list(map(list, map(list, player.cycles))))
        datas.append({
            'cycles': list(map(list, map(list, player.cycles))),
            'dots': list(player.dots),
            'color': player.color
        })
    return datas

def main(request):
    print("main")
    return render(request, 'index.html')

def test(request):
    print("test")
    if request.method == 'POST':
        position = request.POST.get('position')
        position = tuple(map(int, position.split(',')))
        uiInput.make_move(position)
        #gameField.add_new_dot(position)
        datas = show()
        playerSwitcher.switch_player()
        return JsonResponse(data={'data': datas})
    return HttpResponseRedirect('/')




