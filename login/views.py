from django.http import HttpResponse

def index(request):
    return HttpResponse("Login app")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')