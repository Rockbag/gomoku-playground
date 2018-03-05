#!/bin/bash
set -euo pipefail

# The scripts initiates a build for the application.
# Must be run from the root of the application directory.

cd ../backend
docker build -t gomoku-backend .

cd -

cd ../frontend
docker build -t gomoku-frontend .

