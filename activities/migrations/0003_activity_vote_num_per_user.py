# Generated by Django 2.2 on 2020-07-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20200720_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='vote_num_per_user',
            field=models.IntegerField(default=8),
        ),
    ]
