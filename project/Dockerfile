# pull official base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# install python dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# command for heroku
# CMD gunicorn --bind 0.0.0.0:$PORT
CMD uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
