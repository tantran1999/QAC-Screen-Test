FROM python:3.10-bullseye

WORKDIR /root

RUN apt-get update -y
RUN apt-get install -y gcc make python3-dev

COPY ./requirements.txt /root/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api.py /root/api.py

CMD [ "python", "api.py" ]