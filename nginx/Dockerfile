FROM nginxinc/nginx-unprivileged:1-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

