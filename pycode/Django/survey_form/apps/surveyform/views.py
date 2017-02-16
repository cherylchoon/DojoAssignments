from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyform/index.html')

def survey_process(request):
    if request.method == 'POST':
        for key in request.POST:
            request.session[key] = request.POST[key]
        return redirect('/result')

def result(request):
    return render(request, 'surveyform/result.html')
