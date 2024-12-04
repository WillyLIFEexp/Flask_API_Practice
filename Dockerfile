FROM python:3.8-slim
WORKDIR /flask_api
COPY . /flask_api
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
