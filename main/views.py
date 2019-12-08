from django.shortcuts import render
from main import models
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import  PancianoForm, PjovenForm, PninoForm
from django.urls import reverse_lazy
from .models import Hospital, Consulta, Paciente, Panciano, Pjoven, Pnino
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# CONSULTA
class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'

    def get_queryset(self):
        consulta = models.Consulta.objects.all()
        return consulta.all()
    
class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consulta_detail.html'

class ConsultaCreateView(CreateView):
    model = Consulta
    template_name = 'consulta_new.html'
    fields = ('id_consulta', 'cantidad_pacientes', 'nombre_especialista', 'tipo_consulta', 'estado', 'hospitales', )
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'OK!')
        else:
            messages.error(self.request, "Error!")

        return super().form_valid(form)


#PACIENTE

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'paciente'
    
    def get_queryset(self):
        pacientes = models.Paciente.objects.all()
        return pacientes.order_by("-prioridad")

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'


# PNINO
class PninoListView(ListView):
    model = Pnino
    template_name = 'pnino_list.html'
    context_object_name = 'pnino'

class PninoDetailView(DetailView):
    model = Pnino
    template_name = 'pnino_detail.html'

class PninoCreateView(CreateView):
    model = Pnino
    template_name = 'pnino_new.html'
    fields = ('prioridad','nombre', 'edad', 'n_hist_clinica', 'hospitales', 'rel_peso_estatura',)
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'OK!')
        else:
            messages.error(self.request, "Error!")

        return super().form_valid(form)

# PJOVEN
class PjovenListView(ListView):
    model = Pjoven
    template_name = 'pjoven_list.html'
    context_object_name = 'pjoven'

class PjovenDetailView(DetailView):
    model = Pjoven
    template_name = 'pjoven_detail.html'

class PjovenCreateView(CreateView):
    model = Pjoven
    template_name = 'pjoven_new.html'
    fields = ('prioridad','nombre', 'edad', 'n_hist_clinica', 'hospitales', 'fumador',)
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'OK!')
        else:
            messages.error(self.request, "Error!")

        return super().form_valid(form)

# PANCIANO
class PancianoListView(ListView):
    model = Panciano
    template_name = 'panciano_list.html'
    context_object_name = 'panciano'

class PancianoDetailView(DetailView):
    model = Panciano
    template_name = 'panciano_detail.html'

class PancianoCreateView(CreateView):
    model = Panciano
    template_name = 'panciano_new.html'
    fields = ('prioridad','nombre', 'edad', 'n_hist_clinica', 'hospitales', 'tiene_dieta',)
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'OK!')
        else:
            messages.error(self.request, "Error!")

        return super().form_valid(form)

# HOSPITAL
class HospitalListView(ListView):
    model = Hospital
    template_name = 'home_list.html'
    context_object_name = 'hospital'
    queryset = Hospital.objects.all()

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'hospital_detail.html'

class HospitalCreateView(CreateView):
    model = Hospital
    template_name = 'hospital_new.html'
    fields = ('nombre', )
    
    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'OK!')
        else:
            messages.error(self.request, "Error!")

        return super().form_valid(form)