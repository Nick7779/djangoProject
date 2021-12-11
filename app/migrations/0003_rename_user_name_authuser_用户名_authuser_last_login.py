# Generated by Django 4.0 on 2021-12-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_authuser_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authuser',
            old_name='user_name',
            new_name='用户名',
        ),
        migrations.AddField(
            model_name='authuser',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]
