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

RUN apt-get update
RUN apt-get install -y curl \
    sudo \
    make 

# Building frontend ts file.
ENV NVM_DIR=/usr/local/nvm

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN mkdir $NVM_DIR \
    && touch ~/.bashrc ~/.bash_profile

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && source ~/.bash_profile \
    && nvm install \
    && npm install \
    && npm run build

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
