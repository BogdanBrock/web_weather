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
- [] Сделать web приложение, оно же сайт, где пользователь вводит название города, 
и получает прогноз погоды в этом городе на ближайшее время.

Будет плюсом если:
- [] Написаны тесты
- [] Всё это помещено в докер контейнер
- [] Сделаны автодополнение (подсказки) при вводе города
- [] При повторном посещении сайта будет предложено посмотреть погоду в городе, 
в котором пользователь уже смотрел ранее
- [] Будет сохраняться история поиска для каждого пользователя, и будет API, 
показывающее сколько раз вводили какой город

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

- Все маршруты доступны по адресу:
```bash
http://127.0.0.1:8000/docs#/
```
