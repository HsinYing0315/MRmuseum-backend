FROM python:3.9.13
WORKDIR /
ADD . /
RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0