# Generated by Django 2.1.5 on 2020-10-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnz', '0003_auto_20201001_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True),
        ),
    ]