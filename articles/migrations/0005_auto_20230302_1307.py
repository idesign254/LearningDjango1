# Generated by Django 3.0.5 on 2023-03-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(),
        ),
    ]