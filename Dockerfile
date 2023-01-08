FROM python:latest
LABEL maintainer="asabhi6776"

WORKDIR /code
ADD requrements.txt /code/.
RUN pip install --no-cache-dir -r requrements.txt

ADD bot.py /code/.

ENTRYPOINT [ "bash" ]
# ENTRYPOINT [ "python3 bot.py" ]