# Generated by Django 5.0.6 on 2024-10-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user_password',
            field=models.CharField(max_length=50),
        ),
    ]
