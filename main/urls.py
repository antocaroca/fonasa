from django.urls import path
from .views import (
    HospitalListView,
    HospitalDetailView,
    HospitalCreateView,
    ConsultaListView,
    ConsultaDetailView,
    ConsultaCreateView,
    PninoListView,
    PninoDetailView,
    PninoCreateView,
    PjovenListView,
    PjovenDetailView,
    PjovenCreateView,
    PancianoListView,
    PancianoDetailView,
    PancianoCreateView,
    PacienteListView,
    PacienteDetailView,
    
)

urlpatterns = [
    path('hospital/', HospitalListView.as_view(), name='home_list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital_detail'),
    path('new/', HospitalCreateView.as_view(), name='hospital_new'),
    #consulta
    path('consulta/', ConsultaListView.as_view(), name='consulta_list'),
    path('consulta/<int:pk>/', ConsultaDetailView.as_view(), name='consulta_detail'),
    path('new_consulta/', ConsultaCreateView.as_view(), name='consulta_new'),
    #pnino
    path('pnino/', PninoListView.as_view(), name='pnino_list'),
    path('pnino/<int:pk>/', PninoDetailView.as_view(), name='pnino_detail'),
    path('new_pnino/', PninoCreateView.as_view(), name='pnino_new'),
    #pjoven
    path('pjoven/', PjovenListView.as_view(), name='pjoven_list'),
    path('pjoven/<int:pk>/', PjovenDetailView.as_view(), name='pjoven_detail'),
    path('new_pjoven/', PjovenCreateView.as_view(), name='pjoven_new'),
    #panciano
    path('panciano/', PancianoListView.as_view(), name='panciano_list'),
    path('panciano/<int:pk>/', PancianoDetailView.as_view(), name='panciano_detail'),
    path('new_panciano/', PancianoCreateView.as_view(), name='panciano_new'),
        #paciente
    path('paciente/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    
]