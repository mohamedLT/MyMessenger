# Generated by Django 4.0.5 on 2022-06-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='users',
        ),
        migrations.AddField(
            model_name='message',
            name='users',
            field=models.ManyToManyField(to='main.user'),
        ),
    ]
