# Use the official Python image as the base image
FROM python:3.11

# Set the environment variable to unbuffer output
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the project code to the container
COPY . /app/

# give permissions to the entrypoint.sh file
RUN chmod +x /app/entrypoint.sh

# Expose port 7000
EXPOSE 7000