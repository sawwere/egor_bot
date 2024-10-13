FROM python:3

WORKDIR /usr/src/app
ADD . .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt
CMD python ./main.py