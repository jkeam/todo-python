FROM registry.access.redhat.com/ubi9/python-311@sha256:5e0b16be4c129c19675f2e84dad9ce7039421dfd92b3fa7b339353aeaf45f279

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

USER root
RUN dnf -y install httpd

# Copy local code to the container image
WORKDIR $APP_ROOT
COPY . ./

# Install production dependencies
RUN python3 -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
USER 1001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
