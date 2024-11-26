FROM python:3.10-slim

WORKDIR /app

RUN useradd -m appuser

COPY . /app
RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["python", "main.py"]
CMD ["--port", "8000"]