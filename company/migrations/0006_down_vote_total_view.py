# Generated by Django 2.1.5 on 2019-07-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='industry',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='company',
            name='total_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
