#!/bin/bash

function wait_for_postgre {
    wait-for-it.sh db:5432
}

if [ "$1" = 'dev-webserver' ]; then
    # Wait for postsql service to start
    wait_for_postgre
    python manage.py runserver 0.0.0.0:8000
fi