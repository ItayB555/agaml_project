FROM python:3.12-alpine

WORKDIR /backend
COPY . .
RUN apk add libpq-dev
RUN pip install -r ./requirements.txt
EXPOSE 8050
CMD ["python", "app.py"]