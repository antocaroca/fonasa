from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PacienteForm
from django.urls import reverse_lazy
from .models import Hospital, Consulta, Paciente, Panciano, Pjoven, Pnino
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



# CONSULTA

class ConsultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    context_object_name = 'consulta'
    
    def get_context_data(self, **kwargs):
        context = super(ConsultaListView, self).get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.all()
        
        return context

class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consulta_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConsultaDetailView, self).get_context_data(**kwargs)
        #clientPk = self.kwargs['pk']
        context['consulta'] = Consulta.objects.all()
        context['hospital'] = Hospital.objects.all()
        context['paciente'] = Paciente.objects.all()
        context['panciano'] = Panciano.objects.all()
        context['pnino'] = Pnino.objects.all()
        context['pjoven'] = Pjoven.objects.all()
        
        return context

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

# PACIENTE

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'paciente'

    def get_context_data(self, **kwargs):
        context = super(PacienteListView, self).get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.all()
        context['hospital'] = Hospital.objects.all()
        context['consulta'] = Consulta.objects.all()
        context['panciano'] = Panciano.objects.all()
        context['pnino'] = Pnino.objects.all()
        context['pjoven'] = Pjoven.objects.all()
        
        return context

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PacienteDetailView, self).get_context_data(**kwargs)
        #clientPk = self.kwargs['pk']
        context['paciente'] = Paciente.objects.all()
        
        return context

class PacienteCreateView(CreateView):
    model = Paciente
    template_name = 'paciente_new.html'
    fields = ('nombre', 'edad', 'n_hist_clinica', 'hospitales',)
    
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

    def get_context_data(self, **kwargs):
        context = super(HospitalListView, self).get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()
        context['consulta'] = Consulta.objects.all()
        context['paciente'] = Paciente.objects.all()
        context['panciano'] = Panciano.objects.all()
        context['pnino'] = Pnino.objects.all()
        context['pjoven'] = Pjoven.objects.all()
        
        return context

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'hospital_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HospitalDetailView, self).get_context_data(**kwargs)
        #clientPk = self.kwargs['pk']
        context['consulta'] = Consulta.objects.all()
        context['paciente'] = Paciente.objects.all()
        context['panciano'] = Panciano.objects.all()
        context['pnino'] = Pnino.objects.all()
        context['pjoven'] = Pjoven.objects.all()
        
        return context




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