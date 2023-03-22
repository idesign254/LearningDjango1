# Generated by Django 3.0.5 on 2023-03-19 05:38

from django.db import migrations, models
import requisition.models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0013_auto_20230312_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to=requisition.models.get_file_path),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]