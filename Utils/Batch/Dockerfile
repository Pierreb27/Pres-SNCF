FROM python
RUN pip3 install boto3
RUN mkdir /src
COPY . /src 
CMD [“python”, “/src/batchfile.py”]