# Generated by Django 4.1.2 on 2023-01-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='new_image',
            field=models.ImageField(default=None, upload_to='article'),
        ),
    ]
