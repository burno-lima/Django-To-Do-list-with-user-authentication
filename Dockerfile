FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /todo_list

COPY requirements.txt /todo_list/

RUN pip install -r requirements.txt

COPY . /todo_list/
