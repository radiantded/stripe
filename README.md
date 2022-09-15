# Minishop with Stripe

## Установка
Создайте и активируйте виртуальное окружение (опционально)
```
python -m venv venv
source venv/Scripts/activate
```

Установите зависимости
```
pip install -r requirements.txt
```

Создайте суперпользователя
```
python manage.py createsuperuser
```

Запустите проект из корневого каталога
```
python manage.py runserver
```

Сервер будет доступен по адресу 127.0.0.1 (localhost)
Админ панель - 127.0.0.1/admin
