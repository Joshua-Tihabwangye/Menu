# Generated by Django 5.0.6 on 2024-08-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0005_rename_soda_order_softdrink_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
