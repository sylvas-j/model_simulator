############################
## builder stage
######################
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster AS builder

RUN apt-get update && apt-get install -y git libpq-dev gcc \
    python3-dev default-libmysqlclient-dev \
    build-essential

# create virtual env
RUN python -m venv /opt/venv
# activate venv
ENV PATH="/opt/venv/bin:$PATH"
# Copy the requirements file into the container
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

##########################
# Operational stage
###########################
FROM python:3.9-slim-buster
# Set Environment Variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
# Install dependencies for mysqlclients library
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3-dev default-libmysqlclient-dev \
    build-essential libpq-dev &&\
    rm -rf /var/lib/apt/list/*

# Set the working directory to /app
WORKDIR /app
# Making source and static directory
# RUN mkdir /app
RUN mkdir /static
# # Copy the Django project into the container
COPY . /app
# get the virtual env from builder stage
COPY --from=builder /opt/venv /opt/venv

COPY entrypoint.sh .
RUN chmod 755 entrypoint.sh
# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

# Activate venv
ENV PATH="/opt/venv/bin:$PATH"
# Run Django migrations when not using entrypoint file
# RUN --add-host=host.docker.internal:host-gateway
RUN python manage.py makemigrations
RUN python manage.py migrate
# Collect static files
RUN python manage.py collectstatic --no-input

# Expose the default Django port
# EXPOSE ${APP_PORT}

# USER sylvas
# Start the Django development server
CMD ["sh", "-c", "gunicorn models_simulator.wsgi:application --bind 0.0.0.0:${APP_PORT}"]
# ENTRYPOINT ["sh", "-c", "entrypoint.sh"]
