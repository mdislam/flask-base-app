FROM nginx:1.11.3

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

#RUN  rm -rf /etc/nginx/sites-enabled/*
#ADD  sites-enabled/     /etc/nginx/sites-enabled/

RUN rm /etc/nginx/conf.d/default.conf
COPY sites-enabled/webapp.conf /etc/nginx/conf.d/