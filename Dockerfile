FROM python:3.11.3
WORKDIR /usr/src/app
COPY . .
#RUN apt-get update
#RUN apt-get install -y ffmpeg
#RUN mkdir -p ./outputs
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-u", "./main.py"]
