# Base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /sprs_api

# Copy the requirements file to the container
COPY . .