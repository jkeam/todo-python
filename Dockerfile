FROM registry.access.redhat.com/ubi9/python-311@sha256:5e0b16be4c129c19675f2e84dad9ce7039421dfd92b3fa7b339353aeaf45f279

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

USER root
RUN dnf -y install httpd

# Copy local code to the container image
WORKDIR $APP_ROOT
COPY . ./

# Default env vars
ENV PORT 8080

# Install production dependencies
RUN python3 -m pip install --upgrade pip
RUN pip install -r ./requirements.txt
USER 1001

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
