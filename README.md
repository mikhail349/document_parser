# Парсер документов

Использует Google Vision для распознавания.

## Browsable API
1. Парсер чека `http://127.0.0.1:8000/receipts/`

## Локальный DEV запуск

1. Сформировать виртуальное python-окружение `python -m venv venv`
2. Установить зависимости `pip install -r requirements.txt -r requirements.dev.txt`
3. Создать файл `.env` с переменными окружения по аналогии с файлом `.env.example`
4. Выполнить миграции `python manage.py migrate`
5. Запустить dev-сервер `python manage.py runserver`

## Линтинг

1. Запуск `isort . && flake8 && mypy .` Настройки находятся в `setup.cfg`