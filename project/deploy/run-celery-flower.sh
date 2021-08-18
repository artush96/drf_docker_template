#!/bin/bash

# shellcheck disable=SC2034
APP_DIR="/home/sites/toocan_backend"
PYENV_DIR="/home/sites/toocan_backend/venv"

# shellcheck disable=SC2164
cd $APP_DIR

exec ${PYENV_DIR}/bin/celery -A project flower --port=5001