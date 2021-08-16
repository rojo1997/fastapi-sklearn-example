FROM python:3.8 AS FastAPISklearnExample

COPY requirements.txt /FastAPISklearnExample/

WORKDIR /FastAPISklearnExample

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /FastAPISklearnExample

USER daemon

EXPOSE 5000

CMD [ "python", "-u", "app/main.py"]