# Generated by Django 5.0.6 on 2024-08-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0002_lunchorder_supperorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='SodaOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
