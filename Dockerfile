FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /rentapp

COPY requirements.txt /rentapp/

#RUN pip install --upgrade pip

#RUN pip install --upgrade pip 
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install mysqlclient


COPY ./rentcar/ /rentapp/

# Run database migrations
# Expose the port the app runs on
EXPOSE 8000


CMD ["python", "manage.py", "runserver"]
