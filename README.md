## 💻 Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=56C0C0&color=008080)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=56C0C0&color=008080)](https://pydantic-docs.helpmanual.io/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=56C0C0&color=008080)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=56C0C0&color=008080)](https://alembic.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&logo=JSON-web-tokens&logoColor=56C0C0&color=008080)](https://jwt.io/)


## Выполненные пункты
- :heavy_check_mark: Сделать web приложение, оно же сайт, где пользователь 
вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

Будет плюсом если:
- :heavy_check_mark: Написаны тесты
- :heavy_check_mark: Всё это помещено в докер контейнер
- :heavy_check_mark: Сделаны автодополнение (подсказки) при вводе города
- :heavy_check_mark: При повторном посещении сайта будет предложено посмотреть 
погоду в городе, в котором пользователь уже смотрел ранее
- :heavy_check_mark: Будет сохраняться история поиска для каждого пользователя, 
и будет API, показывающее сколько раз вводили какой город

## Инструкция как развернуть проект в докере

- Нужно склонировать проект из репозитория командой:
```bash
git clone git@github.com:BogdanBrock/web_weather.git
```
- Для развертывания проекта, в корне проекта нужно
создать .env файл, можно скопировать данные из .env.example

- Находясь так же в корне проекта нужно перейти
 в папку под названием "docker":
```bash
cd docker
```

- Выполнить команду с включенным докером:
```bash
docker compose up -d
```

- Для того, чтобы запустить тесты, находясь в той же директории выполнить команду:
```bash
docker compose exec app pytest
```

## Дополнительное описание
- Все маршруты доступны по адресу:
```bash
http://127.0.0.1:8000/docs#/
```
- Пересобирать образы для контейнеров не нужно для того, 
чтобы изменить данные, т.к. предусмотрен "bind mounts"