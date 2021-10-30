from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game
# Create your views here.


def start(request):
    if request.method == "POST":
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if option == "1":
            game = Game.objects.filter(room_code=room_code).first()

            if game is None:
                messages.error(request, "Room code doesn't exists")
                return redirect('/tictactoe/start')

            if game is Game.is_over:
                messages.error(request, "Game is finished.")
                return redirect('/tictactoe/start')

            game = Game(game_opponent = username, room_code=room_code)
            opponent = Game.creator_of_the_game 
            game.save()
            context = {
                'opponent' : opponent
            }
            return redirect('/tictactoe/play/' + room_code + '?username=' + username, context)
        else:
            game = Game(creator_of_the_game=username, room_code=room_code)
            game.save()
            opponent = Game.game_opponent
            context = {
                'opponent' : opponent
            }
            return redirect('/tictactoe/play/' + room_code + '?username=' + username, context)

    return render(request, 'tictactoe/home.html')


def play(request, room_code):
    username = request.GET.get('username')
    context = {"room_code": room_code, "username": username}
    return render(request, 'tictactoe/game.html', context)
