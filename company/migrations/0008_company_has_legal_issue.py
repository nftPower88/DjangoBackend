# Generated by Django 2.1.5 on 2020-06-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_company_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='has_legal_issue',
            field=models.BooleanField(default=False),
        ),
    ]
