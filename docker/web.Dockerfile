FROM python:3.6

LABEL AUTHOR="Philip Lin"

ENV SRVHOME=/srv
ENV DJANGO_ROOT=/srv/work

ADD . ${DJANGO_ROOT}
WORKDIR ${DJANGO_ROOT}

RUN pip install -r requirements.txt

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/

RUN cp docker/scripts/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh \
    && chmod 755 /usr/local/bin/wait-for-it.sh /usr/local/bin/docker-entrypoint.sh

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]