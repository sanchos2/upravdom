## Описание

# UPRAVDOM - проект для контроля начислений платежных документов в сфере жкх.

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Django application](https://github.com/sanchos2/upravdom/workflows/Django%20application/badge.svg?branch=master)


## Как деплоить:

Install python3:

```sh
sudo apt install python3
sudo apt install python3-pip
```

Download the project, create virtual environment and activate it, install dependencies:

```sh
git clone https://github.com/sanchos2/upravdom.git
cd upravdom
python3 -m venv venv
source venv/bin/activate.sh
pip3 install -r requirements.txt
```

Make migrations:

```sh
python manage.py migrate
```

Create site admin:

```sh
python manage.py createsuperuser
```

Collect static files to a static root:

```sh
python manage.py collectstatic
```

Add environment variables:

```

```
note: в проде установить Debug в False


## Как запустить:

Run project:

```sh
python manage.py runserver 127.0.0.1:8000
```

Use http://127.0.0.1:8000 to browse a project

## Загрузка исходных данных

Загрузка информации о помещениях

```sh
python manage.py load_placements placements.csv
```

Формат файла placements.csv (загружать без наименования столбцов):

| Тип помещения;Подъезд;Номер квартиры;Общая площадь;Жилая площадь; | 
|-------------------------------------------------------------------| 
| Отдельная квартира;1;1;40.8;16.6;                                 | 
| Нежилое помещение;2;НЖ3;40.8;16.6;                                 | 