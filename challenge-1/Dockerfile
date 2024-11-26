FROM alpine:3.10.1

RUN apk add --no-cache \
    python3=3.7.10-r0

WORKDIR /app

RUN addgroup appuser && \
    adduser --disabled-password --gecos "" --ingroup appuser appuser

COPY . /app

USER appuser
ENTRYPOINT ["python3", "main.py"]
CMD ["--port", "8000"]