# Generated by Django 2.1.7 on 2019-08-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_issue', '0004_auto_20190803_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='IssueRemark',
            field=models.CharField(max_length=10000, null=True, verbose_name='问题备注'),
        ),
    ]
