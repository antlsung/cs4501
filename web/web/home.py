from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, world. Welcome to J's for Bae's.")
