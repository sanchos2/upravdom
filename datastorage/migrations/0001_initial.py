# Generated by Django 3.1.2 on 2021-01-27 09:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер подъезда')),
                ('placement_on_level', models.IntegerField(verbose_name='Количество квартир на этаже')),
                ('total_level', models.IntegerField(verbose_name='Количество этажей в подъезде')),
            ],
            options={
                'verbose_name': 'Подъезд',
                'verbose_name_plural': 'Подъезды',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название дома')),
                ('energy_efficiency', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=2, verbose_name='Энергоэфективность дома')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
        migrations.CreateModel(
            name='IMD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('ГВС', 'ГВС'), ('ХВС', 'ХВС'), ('ЭЛТ_Д', 'ЭЛТ_Д'), ('ЭЛТ_Н', 'ЭЛТ_Н'), ('ТПЛ', 'ТПЛ')], max_length=10, verbose_name='Наименование прибора учета')),
                ('imd_number', models.CharField(max_length=200, verbose_name='Номер прибора учета')),
                ('description', models.TextField(blank=True, verbose_name='Описание прибора учета')),
                ('initial_value', models.IntegerField(default=0, verbose_name='Начальное значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата ввода в эксплуатацию')),
                ('is_active', models.BooleanField(default=True, verbose_name='К учету')),
            ],
            options={
                'verbose_name': 'ИПУ',
                'verbose_name_plural': 'ИПУ',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True, verbose_name='Номер помещения')),
                ('placement_type', models.CharField(choices=[('Отдельная квартира', 'Отдельная квартира'), ('Нежилое помещение', 'Нежилое помещение')], max_length=50, verbose_name='Тип помещения')),
                ('total_space', models.FloatField(blank=True, default=0, null=True, verbose_name='Общая площадь помещения')),
                ('living_space', models.FloatField(blank=True, default=0, null=True, verbose_name='Жилая площадь помещения')),
                ('level', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17)], null=True, verbose_name='Этаж')),
                ('position', models.IntegerField(blank=True, null=True, verbose_name='Позиция на этаже')),
                ('entrance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placements', to='datastorage.entrance', verbose_name='Номер подъезда')),
                ('owner', models.ManyToManyField(blank=True, related_name='placements', to=settings.AUTH_USER_MODEL, verbose_name='Владелец(ы)')),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
                'ordering': ['number', 'total_space', 'placement_type'],
            },
        ),
        migrations.CreateModel(
            name='IMDValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_date', models.DateField(default=datetime.date.today, verbose_name='Дата снятия показания')),
                ('check_value', models.FloatField(verbose_name='Текущее показание')),
                ('imd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imdvalues', to='datastorage.imd', verbose_name='Наименование прибора учета')),
            ],
            options={
                'verbose_name': 'Показание ИПУ',
                'verbose_name_plural': 'Показания ИПУ',
            },
        ),
        migrations.AddField(
            model_name='imd',
            name='placement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imds', to='datastorage.placement', verbose_name='Номер квартиры'),
        ),
        migrations.AddField(
            model_name='entrance',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrances', to='datastorage.house', verbose_name='Название дома'),
        ),
    ]
