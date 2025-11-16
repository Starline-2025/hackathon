FROM nginx:latest

RUN mkdir -p /etc/letsencrypt/live/kartadobra-nko.ru

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/letsencrypt/live/kartadobra-nko.ru/privkey.pem \
    -out /etc/letsencrypt/live/kartadobra-nko.ru/fullchain.pem \
    -subj "/CN=localhost"

COPY dist/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
