# Generated by Django 3.0.5 on 2023-03-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0008_merge_20230228_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
