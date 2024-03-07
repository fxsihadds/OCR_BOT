FROM python:3.11.5-slim

WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire directory into the container
COPY . .

# Grant execution permission to the executable file
RUN chmod +x exefile/VideoSubFinderWXW.exe

EXPOSE 80

# Run bot.py when the container launches
CMD ["python", "main.py"]
