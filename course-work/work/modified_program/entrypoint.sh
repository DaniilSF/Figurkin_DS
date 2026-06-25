#!/usr/bin/env bash
set -e

APP="$1"
if [ -z "$APP" ]; then
  echo "ERROR: Укажи имя файла: docker run IMAGE your_app.py"
  exit 1
fi

exec streamlit run "$APP" --server.address=0.0.0.0 --server.port=8501