from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, team taco. Welcome to CK Real Estate.")