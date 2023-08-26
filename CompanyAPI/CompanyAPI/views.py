from django.http import HttpResponse

def homePage(request):
    print('Home page api called')
    return HttpResponse('<h1>This is your Home Page</h1>')