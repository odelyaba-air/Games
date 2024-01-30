FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
COPY Scores.txt /Scores.txt
ENV NAME World
CMD ["python", "app.py"]

