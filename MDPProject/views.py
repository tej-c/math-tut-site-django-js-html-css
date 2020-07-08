from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def topics(request):
	return render(request, 'topics.html')

def thebasic(request):
	return render(request, 'thebasic.html')

def themoderate(request):
	return render(request, 'themoderate.html')

def theadvanced(request):
	return render(request, 'theadvanced.html')
