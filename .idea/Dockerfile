#baseimage
FROM elytra8/fizfed

COPY . .

# install required pypi modules
RUN pip3 install -r requirements.txt

# Finalization
CMD ["python3","main.py"]
