FROM python:2-onbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
WORKDIR /code/index/
ADD . /code/
