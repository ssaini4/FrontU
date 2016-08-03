from django.shortcuts import render_to_response
  
from blog.models import posts

def home(request):
    entries = posts.objects.all()[:10]
    return render_to_response('index.html', {"posts" : entries})

def login(request):
	return render_to_response('login.html')

def signup(request):
	return render_to_response('signup.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')