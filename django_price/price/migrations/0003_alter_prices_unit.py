# Generated by Django 4.0.3 on 2022-03-20 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
        ('price', '0002_alter_prices_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='unit',
            field=models.ForeignKey(default='98b5cffa-569e-11e0-8b7a-7071bc718fe0', on_delete=django.db.models.deletion.CASCADE, related_name='units', to='unit.units', verbose_name='Единица измерения'),
        ),
    ]
