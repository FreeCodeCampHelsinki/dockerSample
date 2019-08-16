FROM python:3

#This is the folder in the image where the magic happens
WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt

ENV SECRET_KEY=lalalalala

RUN echo "Hello World"

CMD ["python","app.py"]
