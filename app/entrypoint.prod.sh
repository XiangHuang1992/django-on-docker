#!/bin/sh

if ["$DATABASE" = "postgres"]
then
    echo "Waitting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"