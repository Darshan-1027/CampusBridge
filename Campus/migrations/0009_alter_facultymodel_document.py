# Generated by Django 5.2 on 2025-04-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campus', '0008_alter_facultymodel_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultymodel',
            name='Document',
            field=models.ImageField(upload_to='media/Faculty_documents'),
        ),
    ]
