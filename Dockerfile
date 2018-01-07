
FROM python:3.6

WORKDIR /match-our-songs

ADD . /match-our-songs

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
