# Generated by Django 2.1.7 on 2019-07-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommonApps', '0002_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_flag',
            field=models.IntegerField(default=0),
        ),
    ]
