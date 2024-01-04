import boto3
import csv
import io

s3Client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)

    response = s3Client.get_object(Bucket=bucket, Key=key)
    
    data = response['Body'].read().decode()
    reader = csv.reader(io.StringIO(data), delimiter=';')
    next(reader)
    for row in reader:
        print(str.format("Item(s) : {} / Price : {}", row[0], str(int(row[1])*int(row[2]))))