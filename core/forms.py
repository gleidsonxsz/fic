from django import forms
from .models import Curso, Area, Publico

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'vagas', 'carga_horaria', 'data', 'area', 'publico']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'publico': forms.CheckboxSelectMultiple(),
        }