# Проект Управления Заказами и Услугами
Проект предоставляет веб-платформу для управления заказами и услугами, включая регистрацию и аутентификацию пользователей, работу с заказами и опытом пользователей. Платформа разделяет пользователей на заказчиков и исполнителей, предоставляя каждому типу пользователей индивидуальные функциональные возможности. Заказчики могут добавлять заказы, которые исполнители могут принимать и выполнять, увеличивая свой опыт.
## Технологический стек
- Django как основной фреймворк для бэкенда
- PostgreSQL для базы данных
- Docker для контейнеризации и упрощения развертывания
- Python для серверной логики

# Установка и запуск
- Установите Docker и Docker Compose для вашей операционной системы.

# Шаги для запуска
- Клонируйте репозиторий: git clone https://github.com/Stanis4live/Anverali_test
- cd Anverali_test
- Запустите проект с помощью Docker Compose: docker-compose up --build
- После запуска сервер доступен по адресу http://localhost:8000/

# Работа с веб-платформой
Доступ к платформе начинается с домашней страницы, где пользователи могут регистрироваться или входить в систему.
Зарегистрированные пользователи могут входить в свои личные кабинеты, где доступны функции управления профилем и заказами.

# Основные функции платформы
# Аутентификация
- Регистрация пользователя: /signup/
- Вход пользователя: /login/
- Выход пользователя: /logout/
# Кабинет заказчика
- Просмотр и редактирование своего профиля
- Добавление новых заказов
- Накопление опыта за размещение заказов
# Кабинет исполнителя
- Просмотр и редактирование своего профиля
- Выполнение заказов
- Накопление опыта за выполнение заказов
# Дополнительная информация
- Все данные о пользователях и заказах хранятся в базе данных PostgreSQL
- Веб-платформа использует систему шаблонов Django для рендеринга HTML на основе данных из бэкенда



