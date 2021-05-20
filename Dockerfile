FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y libsndfile-dev

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

COPY . /app

RUN pip install -e .

EXPOSE 8881

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8881"]