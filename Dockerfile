FROM continuumio/anaconda3:latest
EXPOSE 5000
COPY . /mario
WORKDIR /mario
RUN pip install -r requirements.txt

CMD ["app.py"]
