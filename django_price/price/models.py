from django.db import models
from catalogs.models import Products
from unit.models import Units
#import uuid


class Prices(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Номенклатура',
                                related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',
                                blank=True, default=0)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, verbose_name='Единица измерения',
                             related_name='units')

    def __str__(self):
        return f'{self.product} - {self.unit} - {self.price} '

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'

