# syntax=docker/dockerfile:1.4
FROM ubuntu:22.04

# Install OS-level packages
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get --yes upgrade && \
    apt-get -y install sudo && \
    apt-get --yes install --no-install-recommends && \
    apt-get install -y postgresql-client \
    python3.10-full tini build-essential 

# Create and activate virtual environment
ENV VIRTUAL_ENV="/root/.venv"
RUN python3.10 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Update pip
RUN pip install --upgrade pip setuptools wheel

# Setup root home directory
WORKDIR /root/take_home_project

# Install package
# COPY backend /root/take_home_project/
COPY . .
RUN pip install . --requirement requirements.txt

ENTRYPOINT ["tini", "-v", "--"]
# EXPOSE 5000
# RUN psql -h localhost -p 5432 -U process_trending -d brx1
# RUN python3 backend/app.py
