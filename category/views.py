from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GraceProjects',
    }
    return render(request, 'category/index.html', context)


def models(request):
    context ={
        'title': '3D-Models',
    }
    return render(request, 'category/models.html', context)


def panarams(request):
    context = {
        'title': 'Съемки 360°',
    }
    return render(request, 'category/shooting.html')


def dron(request):
    context = {
        'title': 'Видео с дрона',
    }
    return render(request, 'category/dron.html', context)



def ar(request):
    context = {
        'title' : 'AR разработка',
    }
    return render(request, 'category/ar.html', context)


def foto(request):
    context = {
        'title': 'Фото-видео съемка',
    }
    return render(request, 'category/foto.html', context)

def vr(request):
    context = {
        'title': 'VR разработка',
    }
    return render(request, 'category/vr.html', context)

def ux(request):
    context = {
        'title': 'UI/UX дизайн',
    }
    return render(request, 'category/ux.html', context)
