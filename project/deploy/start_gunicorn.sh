#!/bin/bash
<<<<<<< HEAD
source /home/sites/project_root/venv/bin/activate
exec gunicorn -c "/home/sites/project_root/project/deploy/gunicorn_config.py" --reload project.wsgi
=======
source /home/sites/toocan_backend/venv/bin/activate
exec gunicorn -c "/home/sites/toocan_backend/project/deploy/gunicorn_config.py" --reload project.asgi -k uvicorn.workers.UvicornWorker
>>>>>>> 432334e47cc34b2c64ed06bb81847615c877fc46
