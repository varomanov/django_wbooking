FROM python:3.11-slim

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаем пользователя для безопасности
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# КОМАНДА ЗАПУСКА - используем SERVIER (ваше имя проекта)
CMD ["gunicorn", "SERVIER.wsgi:application", "--bind", "0.0.0.0:8000"]