# Generated by Django 3.2.4 on 2021-07-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='infomedica',
            field=models.TextField(default=102222),
            preserve_default=False,
        ),
    ]
