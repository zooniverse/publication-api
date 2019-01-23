FROM python:3.7

WORKDIR /usr/src/

COPY requirements.txt /usr/src/

RUN pip install -r requirements.txt

COPY . /usr/src/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
