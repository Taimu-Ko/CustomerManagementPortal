# Dockerfile, Image, Container
FROM python:3.10

# Install app Dependencies
COPY ./requirements.txt /CustomerManagementPortal/requirements.txt

# Create app Director
WORKDIR /CustomerManagementPortal

# Install dependencies and packages
RUN pip install -r requirements.txt

# Bundle app source
COPY . /CustomerManagementPortal

# Configure container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]