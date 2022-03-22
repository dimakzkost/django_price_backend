import uuid
from django.db import models


class Units(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UnitName = models.CharField(verbose_name='Наименование', max_length=20, blank=True)

    def __str__(self):
        return self.UnitName

    class Meta:
        verbose_name = 'Ед.изм.'
        verbose_name_plural = 'Ед.изм.'
