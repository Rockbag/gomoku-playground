FROM ubuntu:xenial

RUN apt-get update && apt-get install -y curl ca-certificates && \
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    nvm install v6.10.0 && \
    mkdir -p /opt/gomoku/gomoku-app/frontend && \
    cd /opt/gomoku/gomoku-app/frontend && \
    npm install -g serve

ADD . /opt/gomoku/gomoku-app/frontend/
RUN chmod u+x /opt/gomoku/gomoku-app/frontend/scripts/start_server.sh \
              /opt/gomoku/gomoku-app/frontend/scripts/build_app.sh

RUN bash /opt/gomoku/gomoku-app/frontend/scripts/build_app.sh

ENTRYPOINT ["bash", "-c", "/opt/gomoku/gomoku-app/frontend/scripts/start_server.sh"]

