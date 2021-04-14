from django import forms
from .models import Post


class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('categoria', 'titulo', 'contenido', 'imagen')