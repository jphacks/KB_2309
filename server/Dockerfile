FROM python:3.8

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--reload"]
