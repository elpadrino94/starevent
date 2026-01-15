from django.shortcuts import redirect, render

from users.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Vérifier que les deux mots de passe correspondent
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            
            if password != password_confirm:
                form.add_error('password_confirm', 'Les mots de passe ne correspondent pas.')
            else:
                # Créer l'utilisateur avec commit=False pour éviter de sauvegarder deux fois
                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
