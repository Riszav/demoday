# Demoday — Auth API

REST API для регистрации и входа пользователей на базе Django REST Framework.

---

## Стек

- **Python** + **Django 4.2**
- **Django REST Framework**
- **SQLite** (база данных)
- **ngrok** (публичный туннель для локального сервера)

---

## Запуск

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Применить миграции

```bash
python manage.py migrate
```

### 3. Запустить сервер

```bash
python manage.py runserver
```

### 4. Открыть публичный доступ через ngrok

```bash
ngrok http 8000
```

После этого ngrok выдаст публичный URL вида `https://xxxx.ngrok.io` — его можно использовать для запросов с любого устройства.

---

## Структура проекта

```
demoday/
├── main/               # Приложение — views, serializers, models
├── demoday/            # Настройки Django и URL-маршруты
├── CD/                 # Практические скрипты (ёлка, auth-демо)
├── manage.py
└── requirements.txt
```
