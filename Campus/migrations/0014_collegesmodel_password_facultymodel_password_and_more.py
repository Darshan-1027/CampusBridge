# Generated by Django 5.2 on 2025-04-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campus', '0013_studentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegesmodel',
            name='Password',
            field=models.CharField(default='dp1234', max_length=15),
        ),
        migrations.AddField(
            model_name='facultymodel',
            name='Password',
            field=models.CharField(default='dp1234', max_length=15),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='Password',
            field=models.CharField(default='dp1234', max_length=15),
        ),
    ]
