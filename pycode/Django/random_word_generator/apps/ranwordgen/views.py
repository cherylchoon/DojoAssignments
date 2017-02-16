from django.shortcuts import render, redirect
import random, string

def index(request):
    if 'user' not in request.session:
        request.session['user'] = 0
    if 'ranstr' not in request.session:
        request.session['ranstr'] = ''
    return render(request, 'ranwordgen/index.html')

def generate(request):
    if request.method == 'POST':
        request.session['ranstr'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(20)])
        request.session['user'] += 1
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
