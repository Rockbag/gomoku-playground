FROM ubuntu:xenial

# Install pip and setup dir structure for app
# Note: pip only works with HTTPS, so we need to install ca-certificates here.
RUN  apt-get update && \
     apt-get install ca-certificates -y && \
     apt-get install python3-pip -y  && \
     apt-get install postgresql postgresql-contrib -y && \
     mkdir -p /opt/gomoku/gomoku-app

ADD . /opt/gomoku/gomoku-app/backend
RUN chmod u+x /opt/gomoku/gomoku-app/backend/scripts/*

# not using virtualenv as the environment is already isolated in the container
RUN cd /opt/gomoku/gomoku-app/backend && \
    pip3 install  -r requirements.txt

