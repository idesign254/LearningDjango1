# Generated by Django 3.2.18 on 2023-03-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0017_document_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='approval',
            field=models.BooleanField(default='Not Approved'),
        ),
    ]