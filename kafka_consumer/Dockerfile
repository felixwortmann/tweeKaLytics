FROM python:3

# ADD request.py /

ADD * /

# ADD requirements.txt /

RUN pip3 install -r requirements.txt

CMD ["python3","./consumer.py"]