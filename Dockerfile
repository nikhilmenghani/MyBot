FROM elytra8/fizfed:latest

RUN pip3 -u -R requirements.txt

CMD ["python3","main.py"]
