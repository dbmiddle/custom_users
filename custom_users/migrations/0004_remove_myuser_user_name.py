# Generated by Django 3.0.6 on 2020-05-20 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_myuser_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_name',
        ),
    ]
