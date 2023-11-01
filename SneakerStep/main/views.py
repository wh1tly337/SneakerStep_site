from django.shortcuts import render


def index(request):
    return render(template_name='main/Home.html', request=request)


def catalog():
    pass
