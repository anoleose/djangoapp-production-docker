from django.shortcuts import render, redirect

from django.template import loader
from django.http import HttpResponse 
from .forms import NewsAddForm 
from .models import News


def home(request):
	news = News.objects.all().order_by('-created_at')
	context = {
		"news":news
	}

	template = loader.get_template('news_app/home.html')
	return HttpResponse(template.render(context, request))


def add_news(request):
	if request.method == "POST":
	    form = NewsAddForm(request.POST)
	    
	    if form.is_valid():
	        form_1 = form.save()
	        return redirect('/')
	else:
	    form = NewsAddForm()

	context = {
	    'form':form,
	    
	}

	template = loader.get_template('news_app/add_news.html')
	return HttpResponse(template.render(context, request))
