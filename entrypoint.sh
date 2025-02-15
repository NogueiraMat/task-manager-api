#!/bin/bash

cd /app/database
alembic upgrade head

cd /app
uvicorn main:app --host 0.0.0.0 --port 8080 --reload