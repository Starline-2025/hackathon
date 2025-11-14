# Используем официальный образ Nginx
FROM nginx:stable-alpine

# Рабочая директория внутри контейнера
WORKDIR /usr/share/nginx/html

# Копируем локальные статические файлы в контейнер
# Например, index.html, CSS, JS и т.д.
COPY ./dist .

# Копируем свой конфиг nginx (если есть)
COPY ./nginx.conf /etc/nginx/nginx.conf

# Порт, который будет слушать контейнер
EXPOSE 80

# Запуск Nginx в фореграунд режиме
CMD ["nginx", "-g", "daemon off;"]
