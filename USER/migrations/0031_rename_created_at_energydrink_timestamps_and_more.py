# Generated by Django 5.1.2 on 2024-12-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0030_notification_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='energydrink',
            old_name='created_at',
            new_name='timestamps',
        ),
        migrations.RenameField(
            model_name='juices',
            old_name='created_at',
            new_name='timestamps',
        ),
        migrations.RenameField(
            model_name='supper',
            old_name='created_at',
            new_name='timestamps',
        ),
        migrations.RenameField(
            model_name='whiskeys',
            old_name='created_at',
            new_name='timestamps',
        ),
    ]
