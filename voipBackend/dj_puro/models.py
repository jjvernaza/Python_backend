from django.db import models

class clientes(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    correo_electronico = models.CharField(max_length=70)
    fecha_instalacion = models.DateField(null=True, default=None)
    tipo_servicio = models.CharField(max_length=12)
    celular = models.CharField(max_length=15)
    MacAdress = models.CharField(max_length=20,null=True, default=None)
    id_plan = models.IntegerField(null=True, default=None)
    act_usua = models.CharField(max_length=10)
    act_hora = models.DateTimeField(null=True, default=None)
    act_esta = models.CharField(max_length=20, default=None)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = "Clientes"



