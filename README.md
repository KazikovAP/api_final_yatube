# API для Yatube

## Описание
API (основанный на Django REST Framework (DRF)) для социальной сети Yatube.

**Реализация:**

- Авторизация по JWT токену (JSON Web Token).
- Сериализация данных для моделей проекта (Group, Post, Follow, Comment).
- Обработка GET, POST, PATCH, PUT и DELETE запросов.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/KazikovAP/api_final_yatube.git
```

```
cd api_yatube
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt в виртуальное окружение:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Применить и выполнить миграции:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Запуск тестов

Из корня проекта:

```
pytest
```

Если все тесты прошли успешно, мои поздравления!

## Эндпоинты проекта

- `api/v1/api-token-auth/` (POST): передать логин и пароль, получить токен.

- `api/v1/posts/` (GET, POST): получить список всех постов или создать новый пост.

- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получить, редактировать или удалить пост по id.

- `api/v1/posts/{post_id}/comments/` (GET, POST): получить список всех комментариев поста с id=post_id или создать новый, указав id поста, который нужно прокомментировать.

- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получить, редактировать или удалить комментарий по id у поста с id=post_id.

- `api/v1/groups/` (GET): получить список всех групп.

- `api/v1/groups/{group_id}/` (GET): получить информацию о группе по id.

- `api/v1/follow/` (GET, POST): Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

- `api/v1/jwt/create/` (POST): Получение JWT-токена.

- `api/v1/jwt/refresh/` (POST): Обновление JWT-токена.

- `api/v1/jwt/verify/` (POST): Проверка JWT-токена.



## Авторы

Aleksey Kazikov

## Лицензия

[MIT](https://opensource.org/licenses/MIT)