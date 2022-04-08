from django.shortcuts import render

# Create your views here.


def Accueil(request):
    return render(request,'accueil.html')

def Connexion(request):
    return render(request,'pageConnexion.html')

def Besoin(request):
    return render(request,'Besoin.html')

def BesoinPending(request):
    return render(request,'BesoinPending.html')

def BesoinValider(request):
    return render(request,'BesoinValider.html')

def BesoinCreation(request):
    return render(request,'BesoinCreation.html')

def MesBesoins(request):
    return render(request,'mesBesoins.html')


def Portfolio(request):
    return render(request,'portfolio.html')