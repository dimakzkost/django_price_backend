# Generated by Django 4.0.3 on 2022-03-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unit', '0001_initial'),
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalogs.products', verbose_name='Номенклатура')),
                ('unit', models.ForeignKey(default='123e4567-e89b-12d3-a456-426655440000', on_delete=django.db.models.deletion.CASCADE, related_name='units', to='unit.units', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Прайс',
                'verbose_name_plural': 'Прайс',
            },
        ),
    ]