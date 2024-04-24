FROM python:alpine 

RUN pip install nltk

WORKDIR /app

COPY app.py ./
COPY requirements.txt ./
COPY paragraphs.txt ./

CMD ["python", "app.py"]
