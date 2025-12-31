from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from events.forms import EventForm
from users.models import User
from events.models import Event


def home(request):
    events = Event.objects.filter(status='PUBLISHED').order_by('-created_at')
    return render(request, 'event/home.html', {'events': events})

def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_auth = authenticate(username=user.username, password=password)

            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, "Connexion réussie.")
                return redirect('home')
            else:
                messages.error(request, "Email ou mot de passe incorrect.")
        except User.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")

    return render(request, 'event/home.html')

def deconnexion(request):
    logout(request)
    return redirect('home')


def create_event(request):
    if request.user.role != 'PROMOTER':
        return redirect('events:list')  # Rediriger si l'utilisateur n'est pas promoteur

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.promoter = request.user
            event.save()
            return redirect('events:list')  # Rediriger vers la liste des événements
    else:
        form = EventForm()

    return render(request, 'events/event_create.html', {'form': form})
