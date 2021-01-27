from datetime import date
from typing import List, Tuple
from django.contrib.auth.models import User
from django.db import models


class House(models.Model):
    """House."""

    choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]  # noqa: WPS221
    title = models.CharField('Название дома', max_length=200)  # noqa: WPS432
    energy_efficiency = models.CharField('Энергоэфективность дома', choices=choices, max_length=2)

    def __str__(self):  # noqa: D105
        return self.title

    class Meta:  # noqa: D106, WPS306

        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Entrance(models.Model):
    """Подъезд (секция)."""

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,  # TODO after test, setmode PROTECT
        related_name='entrances',
        verbose_name='Название дома',
    )
    number = models.IntegerField('Номер подъезда', null=False, unique=True)
    placement_on_level = models.IntegerField('Количество квартир на этаже', null=False)
    total_level = models.IntegerField('Количество этажей в подъезде', null=False)

    def __str__(self):  # noqa: D105
        return f'Подъезд №{self.number}'

    class Meta:  # noqa: D106, WPS306

        ordering = ['number']
        verbose_name = 'Подъезд'
        verbose_name_plural = 'Подъезды'


class Placement(models.Model):
    """Помещения."""

    entrance = models.ForeignKey(
        Entrance,
        on_delete=models.CASCADE,   # TODO after test, setmode PROTECT
        related_name='placements',
        verbose_name='Номер подъезда',
    )
    number = models.CharField('Номер помещения', max_length=20, blank=False, unique=True)  # noqa: WPS432
    placements_choices = [('Отдельная квартира', 'Отдельная квартира'), ('Нежилое помещение', 'Нежилое помещение')]
    placement_type = models.CharField('Тип помещения', max_length=50, choices=placements_choices)  # noqa: WPS432
    total_space = models.FloatField('Общая площадь помещения', null=True, blank=True, default=0)
    living_space = models.FloatField('Жилая площадь помещения', null=True, blank=True, default=0)

    owner = models.ManyToManyField(User, blank=True, related_name='apartments', verbose_name='Владелец(ы)')

    def __str__(self):  # noqa: D105
        return str(self.number)

    levels_choices: List[Tuple[int, int]] = [(i, i) for i in range(1, 18)]  # noqa: WPS111, WPS432  TODO вынести в env var
    level = models.IntegerField('Этаж', choices=levels_choices, null=True, blank=True)
    position = models.IntegerField('Позиция на этаже', null=True, blank=True)

    class Meta:  # noqa: D106, WPS306

        ordering = ['number', 'total_space', 'placement_type']
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'


class IMD(models.Model):
    """Индивидуальные приборы учета (ИПУ)."""

    placement = models.ForeignKey(
        Placement,
        on_delete=models.CASCADE,   # TODO after test, setmode PROTECT
        related_name='imds',
        verbose_name='Номер квартиры',
    )
    type_choices = [('ГВС', 'ГВС'), ('ХВС', 'ХВС'), ('ЭЛТ_Д', 'ЭЛТ_Д'), ('ЭЛТ_Н', 'ЭЛТ_Н'), ('ТПЛ', 'ТПЛ')]  # noqa: WPS221
    title = models.CharField('Наименование прибора учета', max_length=10, choices=type_choices)
    imd_number = models.CharField('Номер прибора учета', max_length=200)  # noqa: WPS432
    description = models.TextField('Описание прибора учета', blank=True)
    initial_value = models.IntegerField('Начальное значение', default=0)
    created_at = models.DateTimeField('Дата ввода в эксплуатацию', auto_now_add=True)
    is_active = models.BooleanField('К учету', default=True)

    def __str__(self):  # noqa: D105
        return f'{self.title}'

    class Meta:  # noqa: D106, WPS306

        ordering = ['title']
        verbose_name = 'ИПУ'
        verbose_name_plural = 'ИПУ'


class IMDValue(models.Model):
    """Данные измерительного прибора на день учета."""

    imd = models.ForeignKey(
        IMD,
        related_name='imdvalues',
        on_delete=models.CASCADE,   # TODO after test, setmode PROTECT
        verbose_name='Наименование прибора учета',
    )
    check_date = models.DateField('Дата снятия показания', default=date.today)
    check_value = models.FloatField('Текущее показание')

    def __str__(self):  # noqa: D105
        return f'{self.imd} {self.check_date} {self.check_value}'

    class Meta:  # noqa: D106, WPS306

        verbose_name = 'Показание ИПУ'
        verbose_name_plural = 'Показания ИПУ'
