FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip

RUN pip3 install  pandas matplotlib seaborn sklearn

WORKDIR /app

COPY Melbourne.py /app
COPY melbourne-housing-market/* /app/melbourne-housing-market/

CMD ["python3","-u","./Melbourne.py"]