# Generated by Django 5.1.2 on 2024-12-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
