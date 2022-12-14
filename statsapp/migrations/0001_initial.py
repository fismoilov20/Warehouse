# Generated by Django 4.1.1 on 2022-10-17 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0004_rename_tel_client_phone'),
        ('userapp', '0002_remove_salesman_task_remove_salesman_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1)),
                ('total', models.PositiveSmallIntegerField()),
                ('payed', models.PositiveSmallIntegerField()),
                ('debt', models.PositiveSmallIntegerField(default=0)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.client')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.product')),
                ('salesman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.salesman')),
            ],
        ),
    ]
