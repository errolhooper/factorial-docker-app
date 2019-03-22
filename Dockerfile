FROM python:2.7
MAINTAINER Errol Hooper "errolhooper@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["factorial_app.py"]
