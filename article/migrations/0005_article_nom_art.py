# Generated by Django 4.1.2 on 2023-01-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nom_art',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
