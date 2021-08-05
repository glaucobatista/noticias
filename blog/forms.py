from django import forms
from .models import Comentario

class EnviarEmailForm(forms.Form):
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    para = forms.EmailField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome','email','descricao')
    
