from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse, HttpResponse
from .serializers import NewsSerializer
from news_app.models import News
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions



def api(request):

	context = {}

	template = loader.get_template('news_api/api.html')
	return HttpResponse(template.render(context, request))


@api_view(['GET'])
def api_views(request):
	api_urls = {
		'List': '/news/', 
		}
	return JsonResponse(api_urls)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def news(request):
	news      = News.objects.all().order_by('-created_at')
	serializer = NewsSerializer(news, many=True)
	context    = {
		'serializer':serializer
	}
	return JsonResponse(serializer.data, safe=False)