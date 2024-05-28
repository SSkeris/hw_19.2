# Generated by Django 5.0.4 on 2024-05-18 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('version_number', models.PositiveIntegerField(verbose_name='Номер версии')),
                ('is_actual', models.BooleanField(default=True, verbose_name='Актуальная')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ['product', 'version_number'],
            },
        ),
    ]