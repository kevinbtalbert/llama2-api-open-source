#!/bin/bash
PORT=$(python -c "import os; print(int(os.environ.get('CDSW_APP_PORT', 8000)))")
uvicorn app:app --host 127.0.0.1 --port $PORT > server.log 2>&1 &
