FROM registry.access.redhat.com/ubi9/python-312:9.6-1749631862 as build
USER 0
COPY pyproject.toml uv.lock .
RUN pip install -U pip && \
    pip install uv && \
    uv sync && \
    uv pip freeze > requirements.txt

# Final uses requirements.txt
FROM registry.access.redhat.com/ubi9/python-312:9.6-1749631862 as final

# install deps
USER 1001
COPY --from=build /opt/app-root/src/requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

# source code
COPY app.py ./

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
