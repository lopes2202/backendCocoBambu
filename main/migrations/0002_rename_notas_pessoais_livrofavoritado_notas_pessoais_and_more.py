# Generated by Django 5.1.1 on 2024-09-15 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='livrofavoritado',
            old_name='notas_Pessoais',
            new_name='notas_pessoais',
        ),
        migrations.AddField(
            model_name='livrofavoritado',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
