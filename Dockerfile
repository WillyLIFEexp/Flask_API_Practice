FROM python:3.8-slim
WORKDIR /flask_api
COPY . /flask_api
COPY app/ /flask_api/app
COPY tests/ /flask_api/tests 
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "app/hello", "run", "--host=0.0.0.0"]
