import boto3

session = boto3.session.Session(region_name= 'eu-west-3')
s3 = session.resource('s3')
bucket = s3.Bucket('s3triggerdemo-pb44')

commands = 0
price = 0
for obj in bucket.objects.all():
    key = obj.key
    if key.split(".")[key.split(".").length] == "csv"
        response = s3Client.get_object(Bucket=bucket, Key=key)
    
        data = response['Body'].read().decode()
        reader = csv.reader(io.StringIO(data), delimiter=';')
        next(reader)
        for row in reader:
            price += int(row[1])*int(row[2])

print(str.format("Total commands : {} / Average price : {}", str(commands), str(price/commands)))