from django.urls import path
from django.http import HttpResponse
def start(request):
    return HttpResponse("Start")
urlpatterns = [path("start/", start(None))]
