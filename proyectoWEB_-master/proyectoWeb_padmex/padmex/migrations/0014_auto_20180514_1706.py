# Generated by Django 2.0.4 on 2018-05-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padmex', '0013_auto_20180514_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='asunto',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
