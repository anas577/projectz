from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ticketing index.")


def home(request):
    return HttpResponse("<h1>Homepage</h1>")