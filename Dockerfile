FROM python:3.8.2

WORKDIR /code

ARG KEY_AUTH
ARG TOKEN_AUTH


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV KEY_AUTH ${KEY_AUTH}
ENV TOKEN_AUTH ${TOKEN_AUTH}

COPY ./requirements/base.txt /code/requirements.txt

RUN echo $KEY_AUTH
RUN echo $TOKEN_AUTH

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
