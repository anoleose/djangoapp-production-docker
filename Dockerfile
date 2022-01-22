FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1


COPY ./requirements.txt /requirements.txt
COPY ./medusa_light /medusa_light
COPY ./scripts /scripts


WORKDIR /medusa_light
EXPOSE 8000

RUN python -m venv /py && \
	/py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home medusa_light && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R medusa_light:medusa_light /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts


ENV PATH="/scripts:/py/bin:$PATH"

USER medusa_light

CMD ["run.sh"]