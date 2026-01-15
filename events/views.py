from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from events.forms import EventForm
from users.models import User
from events.models import Event


#=============================================
# PAGE D'ACCUEIL + LISTE DES ÉVÉNEMENTS
#=============================================
def home(request):
    events = Event.objects.filter(status='PUBLISHED').order_by('-created_at')
    return render(request, 'event/home.html', {'events': events})

# =============================================
# PAGE DE DÉTAIL D'UN ÉVÉNEMENT
# =============================================
def event_detail(request, sulg):
    try:
        event = Event.objects.get(slug=sulg, status='PUBLISHED')
    except Event.DoesNotExist:
        return redirect('home')  # Rediriger vers la page d'accueil si l'événement n'existe pas

    return render(request, 'event/detail_event.html', {'event': event})


#=============================================
# CONNEXION UTILISATEUR
#=============================================
def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            # Vérifier le mot de passe avec la méthode Django
            if user.check_password(password):
                login(request, user)
                messages.success(request, "Connexion réussie.")
                return redirect('home')
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
        except User.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")

    return render(request, 'event/home.html')


#=============================================
# DÉCONNEXION UTILISATEUR
#=============================================
def deconnexion(request):
    logout(request)
    return redirect('home')


#=============================================
# AJOUTER UN ÉVÉNEMENT
#=============================================
def add_event(request):
    if not (request.user.is_superuser or request.user.role == 'PROMOTER'):
        return redirect('home')
    # if request.user.role != 'PROMOTER':
    #     return redirect('home')  # Rediriger si l'utilisateur n'est pas promoteur

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.promoter = request.user
            event.save()
            return redirect('home')  # Rediriger vers la liste des événements
    else:
        form = EventForm()

    return render(request, 'event/add_event.html', {'form': form})
