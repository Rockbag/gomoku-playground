#!/bin/bash

set euo -pipefail

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

cd /opt/gomoku/gomoku-app/frontend/ 
npm run build
