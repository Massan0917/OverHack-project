FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

# torchだけ先に入れる
RUN pip install torch==2.2.0+cpu torchvision==0.17.0+cpu --index-url https://download.pytorch.org/whl/cpu

# requirements入れる
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt --default-timeout=3000

CMD ["python3.9", "/app/main.py"]

