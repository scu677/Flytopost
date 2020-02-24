# Generated by Django 2.2.3 on 2020-02-24 05:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(choices=[('PP', 'Passport'), ('DL', 'Driver license'), ('OT', 'Others')], max_length=100)),
                ('doc_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('MAIL', 'Mail'), ('ELECTRONICS', 'Electronic'), ('COSMETICS', 'Cosmetic'), ('KITCHEN_AID', 'Kitchen Aid'), ('SHOES', 'Shoe'), ('APPAREL', 'Apparel')], max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('picture', models.ImageField(default='', upload_to='user_images')),
                ('address', models.CharField(max_length=254)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=datetime.datetime.today)),
                ('document', models.ManyToManyField(to='core.Document')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=254)),
                ('destination', models.CharField(max_length=254)),
                ('departure_date', models.DateTimeField(verbose_name=datetime.datetime)),
                ('arrival_date', models.DateTimeField(verbose_name=datetime.datetime)),
                ('available_space', models.FloatField(default=0.0)),
                ('delivery_cost', models.FloatField(default=0.0)),
                ('number_of_packages', models.IntegerField()),
                ('number_of_luggage', models.IntegerField()),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('weight', models.CharField(max_length=254)),
                ('created_on', models.DateTimeField(default=datetime.datetime.today)),
                ('delivered_on', models.DateTimeField(default=datetime.datetime.today)),
                ('reciever_name', models.CharField(max_length=254)),
                ('reciever_address', models.CharField(max_length=254)),
                ('package_status', models.CharField(max_length=254)),
                ('package_color', models.CharField(max_length=254)),
                ('package_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
                ('package_type', models.ManyToManyField(to='core.Item')),
            ],
        ),
    ]
