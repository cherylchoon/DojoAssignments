from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    if 'activities' not in request.session:
        request.session['activites'] = []
    return render(request, 'ninjagold/index.html')

def process_money(request):
    request.session['amtGold'] = 0
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M %p')
    if request.method == 'POST':
        building = request.POST['building']
        if building == 'farm':
            request.session['amtGold'] = random.randrange(10,21)
        elif building == 'cave':
            request.session['amtGold'] = random.randrange(5,11)
        elif building == 'house':
            request.session['amtGold'] = random.randrange(2,6)
        elif building == 'casino':
            request.session['amtGold'] = random.randrange(-50,51)

        if request.session['amtGold'] > 0:
            request.session['activities'].insert(0,"Earned " + str(request.session['amtGold']) + " golds from the " + building + " (" + current_date_time + ")")
        else:
            request.session['activities'].insert(0,"Entered a casino and lost " + str(request.session['amtGold']) + " golds... Ouch... " + current_date_time + ")")

        request.session['totalgold'] += request.session['amtGold']
    return redirect('/')
# Create your views here.
