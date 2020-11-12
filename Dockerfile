FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

ENV PATH="${PATH}:/root/.poetry/bin"

#Install Curl
RUN apt-get update && apt-get install -y \
curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# RUN source $HOME/.poetry/env && poetry update && poetry install

#Copy app code
COPY . /app
RUN chmod 755 /app/entrypoint.sh

# run entrypoint
CMD /app/entrypoint.sh