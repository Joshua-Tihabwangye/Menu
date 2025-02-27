# Generated by Django 5.1.1 on 2024-09-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0015_foodorder_delete_breakfast_delete_energydrink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('table_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Energydrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Juices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('table_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Soda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('table_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('food_item', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FoodOrder',
        ),
    ]
