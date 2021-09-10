from django.shortcuts import render
from django.http import HttpResponse
from  .models import Secteurs , SouSecteurs , Site , Camera



# Create your views here.
def home(request):
    secteur = Secteurs.objects.all()
    sousecteur = SouSecteurs.objects.all()
    site = Site.objects.all()
    camera = Camera.objects.all()
    context = {
        'secteurs':secteur,
        'sousecteurs':sousecteur,
        'sites':site,
        'cameras':camera,
        
    }   
    
    return render(request,'base.html',context)