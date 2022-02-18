FROM sriharsharevadi/bidding_app:bidding_app_base
MAINTAINER "Sri Harsha Revadi" <sriharsha.revadi@ibigroup.com>
WORKDIR /opt/app
#COPY docker-scripts/supervisord.conf /etc/supervisor/supervisord.conf
#COPY docker-scripts/nginx.conf /etc/nginx/sites-enabled/
ADD  crypto/requirements.txt  /opt/
RUN pip install -r /opt/requirements.txt
ADD  crypto  /opt/app
#ADD  frontend  /opt/app/frontend
#COPY docker-scripts/env_file /opt/app/frontend/.env.local
#WORKDIR /opt/app/frontend
#RUN npm install
#RUN npm run build
WORKDIR /opt/app
#RUN python manage.py collectstatic --no-input
#RUN chown www-data:www-data -R /opt/app/frontend
EXPOSE 80
#EXPOSE 8000
#CMD ["/usr/bin/python2.7" , "/usr/bin/supervisord"]
CMD ["python" , "manage.py", "runserver", "0.0.0.0:80"]


