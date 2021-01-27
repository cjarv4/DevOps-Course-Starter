FROM python:3.8-slim-buster as base

# Set working directory
WORKDIR /app

# Set environment values
ENV PATH="${PATH}:/root/.poetry/bin"

#Install Curl
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN  apt-get update \
  && apt-get install -y wget gnupg gnupg2 gnupg1 \
  && rm -rf /var/lib/apt/lists/*

# set display port to avoid crash
ENV DISPLAY=:99

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


FROM base as test
# Configure for production
ENV FLASK_ENV=test

RUN pip3 install pytest
RUN pip3 install python-dotenv
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install selenium
RUN pip3 install webdriver-manager

ENTRYPOINT ["poetry", "run", "pytest"]
# CMD [ "--bind", "0.0.0.0:5000" ]  