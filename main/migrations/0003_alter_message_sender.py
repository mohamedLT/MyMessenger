# Generated by Django 4.0.5 on 2022-06-22 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_remove_user_chats_delete_chats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.user'),
        ),
    ]
