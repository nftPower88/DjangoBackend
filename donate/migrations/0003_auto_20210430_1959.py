# Generated by Django 2.1.5 on 2021-04-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20210430_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='coin',
            field=models.CharField(choices=[('LT', 'LTC'), ('ON', 'ONE'), ('TO', 'TOMO'), ('DG', 'DOGE'), ('AD', 'ADA'), ('TR', 'TRX'), ('DT', 'DOT'), ('BU', 'BUST'), ('US', 'USDT'), ('DB', 'DGB'), ('ET', 'ETC'), ('XL', 'XLM'), ('QT', 'QTUM')], max_length=2),
        ),
    ]
