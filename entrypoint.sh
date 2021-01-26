#!/bin/sh

if [ "$FLASK_ENV" = "production" ]
then
    echo "Creating the production environment..."
    cd todo_files
    poetry run gunicorn --bind 0.0.0.0:5000 "app:create_app()"
fi

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the develop environment..."
    cd todo_files
    poetry run flask run --host 0.0.0.0
fi


exec "$@"