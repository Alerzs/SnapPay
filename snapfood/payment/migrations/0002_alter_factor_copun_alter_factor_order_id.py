# Generated by Django 5.1 on 2024-09-07 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='copun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.copun'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='order_id',
            field=models.IntegerField(unique=True),
        ),
    ]
