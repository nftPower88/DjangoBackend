# Generated by Django 2.1.5 on 2019-07-31 19:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='down_vote',
            field=models.ManyToManyField(related_name='answer_down_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='down_vote',
            field=models.ManyToManyField(related_name='question_down_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='total_view',
            field=models.IntegerField(default=0),
        ),
    ]
