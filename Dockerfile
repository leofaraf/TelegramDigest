FROM telegramdigest

COPY channels.xlsx .
COPY settings.py .

ENV TZ Europe/Moscow

ENV PYTHONIOENCODING utf8

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["python", "main.py"]