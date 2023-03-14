# Generated by Django 3.0.5 on 2023-03-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0012_auto_20230312_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_file',
            field=models.FileField(default='', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
