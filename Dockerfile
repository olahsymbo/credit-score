FROM python:3.7-slim
ENV PYTHONPATH=/usr/lib/python3.7/site-packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y git \ 
    python3-pip \
    && apt-get clean \
    && apt-get autoremove 
RUN mkdir /credit-score
WORKDIR /credit-score
COPY . /credit-score      
RUN pip3 install -r requirements.txt 
EXPOSE 5050
CMD exec gunicorn --bind :5050 --workers 4 --threads 8 wsgi:app
