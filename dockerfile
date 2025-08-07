FROM python:3.9-slim

WORKDIR .

COPY req.txt /req.txt

RUN pip install --no-cache-dir --upgrade -r /req.txt

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8008"]