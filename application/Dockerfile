FROM python:3.7

COPY ./* ./app/

WORKDIR /app/

# upgrade pip
RUN pip install --upgrade pip

# Install pip requirements
# RUN python -m pip install -r /app/requirements.txt

CMD ["python3", "run.py"]
