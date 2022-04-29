from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):  
    return render(request, 'recipes/home.html',context={
        'name':'mostra como passa por parametro no render'
    })


def sobre(request):
    return HttpResponse('sobre')

        
def contato(request):
    return render(request ,'temp/temp.html')
