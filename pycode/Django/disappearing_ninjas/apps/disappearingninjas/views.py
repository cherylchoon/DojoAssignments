from django.shortcuts import render

def index(request):
    return render(request, 'disappearingninjas/index.html')

def ninjas(request):
    return render(request, 'disappearingninjas/ninjas.html')

def ninja_color(request, ninja_color):
    not_color = False
    if ninja_color != 'blue' or ninja_color != 'red' or ninja_color != 'orange' or ninja_color != 'purple':
        not_color = True
    context = {
        'ninja_color': ninja_color,
        'wrong_color': not_color
    }
    return render(request, 'disappearingninjas/ninjas.html', context)
