# Generated by Django 5.2.3 on 2025-06-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='role',
            field=models.CharField(choices=[('RH', 'Ressources Humaines'), ('DIRECTOR', 'Directeur'), ('EMPLOYEE', 'Employé')], default='EMPLOYEE', max_length=20),
        ),
    ]
