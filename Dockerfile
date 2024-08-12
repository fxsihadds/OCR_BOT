FROM python:3.11.5-alpine

WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire directory into the container
COPY . .

EXPOSE 80

# Run bot.py when the container launches
CMD ["python", "main.py"]
