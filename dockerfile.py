FROM python:3.9-slim
WORKDIR/app
COPY cpu_task.py
CMD["python","cpu_task.py"]