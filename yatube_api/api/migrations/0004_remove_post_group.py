# Generated by Django 2.2.6 on 2021-06-27 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]
