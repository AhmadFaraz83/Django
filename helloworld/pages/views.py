from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Welcome Home!")
