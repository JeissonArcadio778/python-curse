FROM python:3.8

WORKDIR /game
COPY requirements.txt /game/requirements.txt

RUN pip install --upgrade -r /game/requirements.txt

COPY ./ /game

CMD bash -c "while true; do sleep 1; done"