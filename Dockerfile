FROM python:3.8-slim-buster as base

# Set working directory
WORKDIR /app

# Set environment values
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

# Install poetry files
RUN poetry install

# run entrypoint
CMD /app/entrypoint.sh


FROM base as production
# Configure for production
ENV FLASK_ENV=production    

FROM base as development
# Configure for local development
ENV FLASK_ENV=development