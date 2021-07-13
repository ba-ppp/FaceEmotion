FROM python:3.9.6

WORKDIR /code

COPY requirements.txt /code

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "retrain.py"]