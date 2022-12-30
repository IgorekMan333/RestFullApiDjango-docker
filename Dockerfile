FROM python

ENV PYTHOUNBUFFERED=1

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
