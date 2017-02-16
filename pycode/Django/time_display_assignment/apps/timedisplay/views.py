from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    date_and_time = datetime.now().strftime('%B %d, %Y %H:%M %p')
    context = {
    'date':date_and_time
    }
    return render(request, 'timedisplay/index.html', context)
