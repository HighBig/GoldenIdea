# Generated by Django 2.2 on 2020-06-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20200603_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='is_accepted',
        ),
        migrations.AddField(
            model_name='idea',
            name='status',
            field=models.IntegerField(choices=[(0, '未采纳'), (1, '已采纳')], default=0),
        ),
    ]
