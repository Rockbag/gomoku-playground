set -euox pipefail

cd /opt/gomoku/gomoku-app/backend
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080

