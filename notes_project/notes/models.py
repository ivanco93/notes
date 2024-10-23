from django.db import models

class Note(models.Model):
    class Meta:
        db_table = 'notes'

    class Status(models.TextChoices):
        COMPLETADO = 'COMPLETED', 'Completado'
        PENDIENTE = 'PENDING', 'Pendiente'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDIENTE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title