# Minishop with Stripe

## Установка
* Создайте и активируйте виртуальное окружение (опционально)
```
python -m venv venv
source venv/Scripts/activate
```

* Установите зависимости
```
pip install -r requirements.txt
```

* Задайте переменные окружения в корневом каталоге в файле .env
```
STRIPE_API_KEY - ключ API Stripe
DJANGO_SECRET_KEY - секретный ключ Django
```

* Создайте суперпользователя
```
python manage.py createsuperuser
```

* Запустите проект из корневого каталога
```
python manage.py runserver
```

* Сервер будет доступен по адресу 127.0.0.1:8000 (localhost)
* Админ панель - 127.0.0.1:8000/admin
