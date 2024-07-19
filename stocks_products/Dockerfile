FROM python:3.9-alpine


# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=stocks_products.settings


# Установка зависимостей
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev

# Обновление пакетного менеджера и установка Nano
RUN apk update && apk add --no-cache nano

# Устанавливаем рабочую директорию в контейнере
WORKDIR /stocks_products

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /stocks_products/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /stocks_products/

# Установка gunicorn
# RUN pip install gunicorn

RUN apk update && apk add --no-cache postgresql-client

CMD ["gunicorn", "--bind", "0.0.0.0:6666", "stocks_products.wsgi:application"]



