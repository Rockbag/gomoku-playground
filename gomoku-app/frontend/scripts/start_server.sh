#!/bin/bash

set euo -pipefail

cd /opt/gomoku/gomoku-app/frontend/

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

serve -s build

