# Generated by Django 4.0.10 on 2023-05-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=24, unique=True),
        ),
    ]