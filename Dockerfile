FROM python:3.8-slim-buster as base

# Set working directory
WORKDIR /app

# Set environment values
ENV PATH="${PATH}:/root/.poetry/bin"

#Install Curl
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Install poetry files
COPY poetry.lock /app
COPY pyproject.toml /app
COPY poetry.toml /app
RUN poetry install

#Copy app code
COPY todo_files /app

EXPOSE 80

FROM base as production
# Configure for production
ENV FLASK_ENV=production  

ENTRYPOINT [ "poetry", "run", "gunicorn", "app:create_app()" ]
CMD [ "--bind", "0.0.0.0:5000" ]  


FROM base as development
# Configure for local development
ENV FLASK_ENV=development

WORKDIR /app/todo_files
ENTRYPOINT [ "poetry", "run", "flask", "run" ]
CMD [ "--host", "0.0.0.0" ]  