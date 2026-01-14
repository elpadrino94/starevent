from django.urls import path
from events import views

# app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('create/', views.add_event, name='add_event'),
]

