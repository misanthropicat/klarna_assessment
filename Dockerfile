FROM python:3.10.4-slim-buster
WORKDIR ./
COPY tests/* ./
COPY *.py ./
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]