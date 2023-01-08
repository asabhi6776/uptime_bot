FROM python:latest
LABEL maintainer="asabhi6776"

WORKDIR /code
ADD requirements.txt /code/.
RUN pip install --no-cache-dir -r requirements.txt

ADD bot.py /code/.

ENTRYPOINT [ "bash" ]
# ENTRYPOINT [ "python3 bot.py" ]