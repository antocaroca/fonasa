from django.urls import path
from .views import (
    HospitalListView,
    HospitalDetailView,
    HospitalCreateView,
    ConsultaListView,
    ConsultaDetailView,
    ConsultaCreateView,
    PacienteListView,
    PacienteDetailView,
    PacienteCreateView,
)

urlpatterns = [
    path('hospital/', HospitalListView.as_view(), name='home_list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital_detail'),
    path('new/', HospitalCreateView.as_view(), name='hospital_new'),
    #consulta
    path('consulta/', ConsultaListView.as_view(), name='consulta_list'),
    path('consulta/<int:pk>/', ConsultaDetailView.as_view(), name='consulta_detail'),
    path('new_consulta/', ConsultaCreateView.as_view(), name='consulta_new'),
    #paciente
    path('paciente/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('new_paciente/', PacienteCreateView.as_view(), name='paciente_new'),
]