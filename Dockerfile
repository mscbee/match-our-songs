
FROM python:3.6

WORKDIR /match-our-songs

ADD . /match-our-songs

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
