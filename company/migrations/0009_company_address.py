# Generated by Django 2.1.5 on 2020-10-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_company_has_legal_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
