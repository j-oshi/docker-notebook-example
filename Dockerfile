# Version 3.11 not compatible at the moment downgrade to 3.!0
FROM python:3.10-slim-buster 

COPY . ./app

COPY setup.py /app

RUN pip install --upgrade pip && pip install --upgrade setuptools

RUN pip install -r ./app/requirements.txt

COPY src /app/src

WORKDIR /app

CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]
