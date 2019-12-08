from django import forms
from main.models import Hospital, Consulta, Paciente

class PacienteForm(forms.ModelForm):
    

    class Meta: 
        model =  Paciente
        fields = ('nombre', 'edad', 'n_hist_clinica', 'hospitales',)