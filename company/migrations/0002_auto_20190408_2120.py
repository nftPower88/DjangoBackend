# Generated by Django 2.1.5 on 2019-04-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
