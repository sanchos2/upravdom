###########
# BUILDER #
###########

FROM python:3.10.0b2-alpine as builder
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY . .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements-prod.txt

#########
# FINAL #
#########

FROM python:3.10.0b2-alpine
RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements-prod.txt .
RUN pip install --no-cache /wheels/*
# COPY ./entrypoint.prod.sh $APP_HOME
COPY . $APP_HOME
RUN chown -R app:app $APP_HOME
USER app
# ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]