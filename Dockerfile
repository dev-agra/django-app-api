FROM python:3.7-alpine3.16

# /tmp means this directory hence is mandatory to add before any working file
#  defining maintainer person maintaining
LABEL maintainers="devansh"

# specify env for running python in docker container
ENV PYTHONBUFFERED 1

# copy req.txt , copy app dir, set working directory, 
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# builds argument as DEV and sets it as false to default
ARG DEV=false

# install dependencies run commands
RUN python -m venv /py && \ 
    #below commands to upgrade pip and install dependencies
    /py/bin/pip install --upgrade pip && \
    # installing the postgresql client
    apk add --update --no-cache postgresql-client && \
    # similar but with virtual, virtual dependencies groups packesg into tmp-build-deps
    apk add --update --no-cache --virtual .tmp-build-deps \
    # packages to install
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    # when DEV is true docker installs requirements.dev dependencies i.e. the development dependencies
    # else production dependencies are installed requirements.dev.txt
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # extra dependencie
    rm -rf /tmp && \
    # removes the packages installed earlier[lightweight and clean docker image]
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Environment variable excetuables to run
ENV PATH="/py/bin:$PATH"

# Registering the user
USER django-user