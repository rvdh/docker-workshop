FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pwgen.py .
VOLUME /volume
CMD ["python", "pwgen.py"]
