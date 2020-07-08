from django.shortcuts import render, HttpResponse
from .models import Contact


# Create your views here.
def home(request):
	if(request.method=="POST"):
		contact = Contact()
		contact.name = request.POST['name']
		contact.email = request.POST['email']
		contact.message = request.POST['message']
		contact.save()

		return render(request, 'index.html', {'message':"You request has been sent"})


	return render(request, 'index.html')