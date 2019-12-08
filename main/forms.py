from django import forms
from main.models import Hospital, Consulta, Paciente, Panciano, Pjoven, Pnino

class PjovenForm(forms.ModelForm):
    edad = forms.IntegerField(min_value=16, max_value=40)

    class Meta: 
        model =  Pjoven
        fields = ('prioridad', 'nombre', 'edad', 'n_hist_clinica', 'hospitales', 'fumador',)

class PancianoForm(forms.ModelForm):
    edad = forms.IntegerField(min_value=41, max_value=100)
    class Meta: 
        model =  Panciano
        fields = ('prioridad', 'nombre', 'edad', 'n_hist_clinica', 'hospitales', 'tiene_dieta',)


class PninoForm(forms.ModelForm):
    edad = forms.IntegerField(min_value=1, max_value=15, label="edad nino", widget=forms.NumberInput(
                attrs={'size':'10'}))
    class Meta: 
        model =  Pnino
        fields = ('prioridad', 'nombre', 'edad', 'n_hist_clinica', 'hospitales', 'rel_peso_estatura',)
