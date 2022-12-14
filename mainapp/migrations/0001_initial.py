# Generated by Django 4.1 on 2022-10-11 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('units', models.CharField(max_length=50)),
                ('income_date', models.DateField(auto_now_add=True)),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.salesman')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('debt', models.PositiveSmallIntegerField(default=0)),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.salesman')),
            ],
        ),
    ]
