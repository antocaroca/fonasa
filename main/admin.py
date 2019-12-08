from django.contrib import admin
from django.utils.html import format_html
from .models import Hospital, Consulta, Paciente, Panciano, Pnino, Pjoven



admin.site.register(Hospital)
admin.site.register(Consulta)
admin.site.register(Paciente)
admin.site.register(Panciano)
admin.site.register(Pnino)
admin.site.register(Pjoven)