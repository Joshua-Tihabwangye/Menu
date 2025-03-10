# Generated by Django 5.1.2 on 2025-01-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0034_rename_chipsitem_edit_chipsitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(max_length=10)),
                ('food_type', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='edit_fast_foodsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Burgers', 'Burgers'), ('Taccos', 'Taccos'), ('Pizza', 'Pizza'), ('Sand Wiches', 'Sand Wiches')], default='Choose Category', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(max_length=10)),
                ('food_type', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sand_wich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(max_length=10)),
                ('food_type', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taccos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(max_length=10)),
                ('food_type', models.CharField(max_length=255)),
                ('number_of_people', models.IntegerField()),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='beers',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='chips_masala',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='energydrink',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='juices',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='plain_chips',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='soda',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='supper',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='water',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='whiskeys',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='wines',
            name='table_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
