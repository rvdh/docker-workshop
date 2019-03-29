FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pwgen.py .
CMD ["python", "pwgen.py"]
