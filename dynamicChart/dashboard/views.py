from django.shortcuts import render
from .models import Lession,LessionScore
from .forms import LessionForm

# Create your views here.

def indexView(request):

    lessions=Lession.objects.all()

    lessionScore=LessionScore()

    if request.method=='POST':
        form=LessionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LessionForm()

    context={

        'lessions':lessions,
        'form':form,
        'chartdata':lessionScore.avrage()
    }
    return render(request,"dashboard/index.html",context) 
     
