# Описание
**Цель тестового задания:**
Определить возможность самообучения кандидата, а так же понимание процесса работы web-приложений на Python.приложений на Python.
Задание:
Написать простой метод «Загрузчик изображений».

**Функционал:**
Загрузка изображений (доступно авторизованному пользователю при наличии аутентификации). Аутентификация и авторизация (на выбор кандидата).

**Сценарий работы API:**
Метод API принимает одно или несколько изображений и сохраняет их в папку. Для передачи использовать POST запрос с содержимым multipart/form-data. Для отправки multipart/form-data использовать REST Client (на выбор кандидата).

**Дополнительные требования:**

 - Валидация загружаемых изображений — максимальный размер 200кб.
 - Изображение должно быть сохранено с уникальным названием.

Для разработки метода использовать— python >= 3.6.5, остальное на выбор кандидата.
При использовании фреймворков — использовать Django. Код проекта должен быть загружен в репозиторий (на выбор кандидата).


**Используемый стек:**

 - Python 3
 - Django Rest Framework
 - PostgreSQL 

# Установка без docker

1. Скопируйте репозиторий
2. Создайте виртальное окружение
```
$ python3 -m venv venv
```
3. Активируйте виртуальное окружение
```
$ source venv/bin/activate
```
4. Установите зависимости
```
$ pip install -r requirements.txt
```
5. Создайте базу данных в PostgreSQL
6. Подключите базу данных в `django_uploader/settings.py`
7. Проведите миграции
```
$ python3 manage.py migrate
```
8. Создайте суперпользователя
```
$ python3 manage.py createsuperuser
```
9. Запустите сервер
```
$ python3 manage.py runserver
```

# Установка через docker

1. Клонируйте репозиторий
2. Откройте консоль и перейдите в папку репозитория
3. Соберите docker-контейнер
```
$ docker-compose build
```
4. Запустите собранный контейнер
```
$ docker-compose up -d
```
5. Данная команда показывает список активных контейнеров
```
$ docker-compose ps
```
6. Проведите миграции
```
$ docker-compose exec web python3 manage.py migrate --noinput
```
7. Создайте суперпользователя
```
$ docker-compose exec web python3 manage.py createsuperuser
```
8. Данная команда показывает все установленные докер-контейнеры
```
$ docker-compose images
```
9. Данная команда останавливает и удаляет все докер-контейнеры
```
$ docker-compose down
```

# Эксплуатация

**Используйте postman для создания запросов.**
(Информация не валидна, обнаружен ряд ошибок. В скором времени информация будет обновлена)

**Регистрация пользователя:**
 - Создайте POST запрос на адрес http://127.0.0.1:8000/auth/users/
 - Во вкладке **body** выберете тип **form-data**
 - Укажите **key** - usrname, password, email, и **value** соответственно
![Alt-текст](https://github.com/StFavn/ImageUploader/blob/main/1.png?raw=true)

**Загрузка изображения**
 - Создайте POST запрос на адрес http://127.0.0.1:8000/upload/
 - Во вкладке **Authorization** выберете тип **Basic Auth**
 - Укажите username, password
![Alt-текст](https://github.com/StFavn/ImageUploader/blob/main/2.1.png?raw=true)
 - Во вкладке **body** выберете тип **form-data**
 - Укажите **key** - image, укажите **тип поля** - file, выберете изображение для отправки
![Alt-текст](https://github.com/StFavn/ImageUploader/blob/main/2.2.png?raw=true)

**Просмотр загруженных изображений**
 - Создайте GET запрос на адрес http://127.0.0.1:8000/gallery/
 - Во вкладке **Authorization** выберете тип **Basic Auth**
 - Укажите username, password
![Alt-текст](https://github.com/StFavn/ImageUploader/blob/main/3.png?raw=true)
