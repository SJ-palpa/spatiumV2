from django.contrib import admin
from django.urls import path

from website.views import *

app_name = 'Website'

urlpatterns = [
    path('', Accueil,),
    path('accueil', Accueil, name='accueil'),
    path('connexion', Connexion, name='connexion'),
    path('besoin', Besoin, name='besoin'),
    path('besoinPending', BesoinPending, name='besoinPending'),
    path('besoinValider', BesoinValider, name='besoinValider'),
    path('besoinCreation',BesoinCreation, name= 'besoinCreation'),
    path('mesBesoins', MesBesoins, name=',mesBesoin'),
    path('portfolio', Portfolio, name='portfolio'),
]