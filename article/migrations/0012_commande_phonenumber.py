# Generated by Django 4.1.3 on 2023-01-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_remove_commande_email_commande_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='phonenumber',
            field=models.CharField(default='', max_length=10),
        ),
    ]
