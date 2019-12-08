from django.db import models
from django.urls import reverse

TIPO_CONSULTA = [
    ('Pediatría', 'Pediatría'),
    ('Urgencia', 'Urgencia'),
    ('Consulta General Integral', 'Consulta General Integral'),
]   

ESTADO = [
    ('Ocupada', 'Ocupada'),
    ('Espera', 'Espera de atención'),
]

class Hospital(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitales'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('hospital_detail', args=[str(self.id)])

class Consulta(models.Model):
    id_consulta = models.PositiveIntegerField()
    cantidad_pacientes = models.PositiveIntegerField()
    nombre_especialista = models.CharField(max_length=60)
    tipo_consulta = models.CharField(max_length=50, choices=TIPO_CONSULTA)
    estado = models.CharField(max_length=50, choices=ESTADO)
    hospitales = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ('pk',)

    def __str__(self):
        return self.nombre_especialista

    def get_absolute_url(self):
        return reverse('consulta_detail', args=[str(self.id)])

class Paciente(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.PositiveIntegerField()
    n_hist_clinica = models.PositiveIntegerField("N° historia clínica")
    hospitales = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    class Meta:
       
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ('pk',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('paciente_detail', args=[str(self.id)])

class Panciano(Paciente):
    tiene_dieta = models.BooleanField(default=False, help_text='Tiene dieta')

    class Meta:
       
        verbose_name = 'Panciano'
        verbose_name_plural = 'Pancianos'
        ordering = ('pk',)

    def __str__(self):
        return self.tiene_dieta

class Pnino(Paciente):
    rel_peso_estatura = models.PositiveIntegerField(help_text="Relación peso/estatura")

    class Meta:
       
        verbose_name = 'Pnino'
        verbose_name_plural = 'Pninos'
        ordering = ('pk',)

    def __str__(self):
        return self.rel_peso_estatura

class Pjoven(Paciente):
    fumador = models.BooleanField(default=False, help_text='fumador')

    class Meta:
       
        verbose_name = 'Pjoven'
        verbose_name_plural = 'Pjovenes'
        ordering = ('pk',)

    def __str__(self):
        return self.fumador

