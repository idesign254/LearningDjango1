# Generated by Django 3.2.18 on 2023-03-30 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0019_alter_document_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
    ]
