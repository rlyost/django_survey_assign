from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'survey_app/index.html')

def process(request):
    if request.method == "POST": 
        request.session['context'] = {"name": request.POST['name'], "location": request.POST['location'], "language": request.POST['language'], "comment": request.POST['comment']}

        print request.session['context']

        return redirect('/result')

    return redirect("/")

def result(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return render(request, 'survey_app/result.html', request.session['context'])
