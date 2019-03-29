FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pwgen.py .
VOLUME /volume
ENV FLASK_APP=pwgen.py
CMD ["flask", "run", "--host=0.0.0.0"]
