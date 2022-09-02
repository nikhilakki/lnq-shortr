# Copyright (c) 2022 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM python:3.10-alpine
RUN apk update && apk upgrade
RUN pip install -U pip poetry==1.1.13
WORKDIR /app
COPY . .
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD ["main.py"]
