from django.urls import path
from events import views



urlpatterns = [
    path('', views.home, name='home'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('create/', views.create_event, name='create_event'),
]

