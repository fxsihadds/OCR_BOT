FROM python:3.11.5-slim

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Run bot.py when the container launches
CMD ["python", "main.py"]
