# Generated by Django 5.1 on 2024-09-09 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_remove_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trans_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
