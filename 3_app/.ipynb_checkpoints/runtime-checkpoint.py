import subprocess
import os
# print(subprocess.run(["sh 3_app/runtime.sh"], shell=True))

# At the end of your runtime.py
subprocess.Popen([
    "uvicorn",
    "app:app",
    "--host", "127.0.0.1",
    "--port", str(os.environ.get('CDSW_APP_PORT', 8000))
])
