import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON = 'PRIV'
    TORG_PRED = 'TORG_PRED'
    COMPANY_PRIVATE = [
        (COMPANY, 'Юридическое лицо (контрагент компании)'),
        (PRIVATE_PERSON, 'Физическое лицо  (розничный покупатель)'),
        (TORG_PRED, 'Торговый представитель')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    IIN = models.CharField(verbose_name="БИН / ИИН", max_length=12, unique=False, null=True, blank=True,
                           help_text='БИН или ИИН указывают юр. лица и ИП. Физические лица не заполняют.')
    phone = models.CharField(max_length=16, unique=False, verbose_name='Номер телефона', blank=True,
                         help_text='Действующий номер телефона')
    full_name = models.CharField(verbose_name="Наименование полное", max_length=250,
                                 unique=True, null=True, blank=True,
                                 help_text='Фамилия и инициалы для физических лиц. Название предприятия для юридических лиц.')
    delivery_adress = models.CharField(verbose_name="Адрес доставки", max_length=250,
                                 unique=False, null=True, blank=True,
                                 help_text='Ваш обычный адрес для доставки заказа.')
    status = models.CharField(verbose_name="Статус клиента", max_length=50, choices=COMPANY_PRIVATE, default=COMPANY,
                              help_text='Юр.лицо - оформляется несколько документов при продаже (счет-фактура, накладная, кассовый чек). Физическое лицо - кассовый чек (как при обычной покупке в магазине)'
    )


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)