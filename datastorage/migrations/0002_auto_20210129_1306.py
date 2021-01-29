# Generated by Django 3.1.2 on 2021-01-29 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datastorage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GHM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование прибора учета')),
                ('ghm_number', models.CharField(max_length=200, verbose_name='Номер прибора учета')),
                ('description', models.TextField(blank=True, verbose_name='Описание прибора учета')),
                ('initial_value', models.IntegerField(default=0, verbose_name='Начальное значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата ввода в эксплуатацию')),
                ('is_active', models.BooleanField(default=True, verbose_name='К учету')),
                ('placement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ghms', to='datastorage.house', verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'ОДПУ',
                'verbose_name_plural': 'ОДПУ',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='placement',
            options={'ordering': ['number'], 'verbose_name': 'Помещение', 'verbose_name_plural': 'Помещения'},
        ),
        migrations.CreateModel(
            name='GHMValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField(default=datetime.date.today, verbose_name='Дата снятия показания')),
                ('check_value', models.FloatField(verbose_name='Текущее показание')),
                ('imd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ghmvalues', to='datastorage.ghm', verbose_name='Наименование прибора учета')),
            ],
            options={
                'verbose_name': 'Показание ОДПУ',
                'verbose_name_plural': 'Показания ОДПУ',
            },
        ),
    ]