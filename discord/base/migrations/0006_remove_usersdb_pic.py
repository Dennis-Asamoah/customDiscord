# Generated by Django 3.2.11 on 2022-01-28 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_usersdb_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdb',
            name='pic',
        ),
    ]
