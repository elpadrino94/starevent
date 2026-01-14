
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'slug', 'description', 'start_datetime', 'end_datetime', 'location', 'city', 'category', 'image', 'status']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Concert Live'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: concert-live-lome'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Décrivez votre événement...', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Palais des Congrès'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Lomé'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sélectionnez le statut'}),
        }
