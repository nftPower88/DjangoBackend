# Generated by Django 2.1.5 on 2020-06-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20200522_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyreview',
            name='has_legal_issue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interview',
            name='has_legal_issue',
            field=models.BooleanField(default=False),
        ),
    ]
