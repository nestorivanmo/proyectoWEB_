# Generated by Django 2.0.4 on 2018-05-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padmex', '0010_auto_20180514_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='asunto',
            field=models.CharField(default=' ', max_length=30),
        ),
    ]
