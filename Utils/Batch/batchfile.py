import boto3
import csv
import io

s3 = boto3.resource('s3')
bucket = s3.Bucket('s3triggerdemo-pb44')

commands = 0
price = 0
for obj in bucket.objects.all():
    key = obj.key
    if key.split(".")[-1] == "csv" :
        commands += 1
        data = obj.get()['Body'].read().decode()
        reader = csv.reader(io.StringIO(data), delimiter=';')
        next(reader)
        for row in reader:
            price += int(row[1])*int(row[2])
        print(str.format("Command {} treated", key))
    else :
        print(str.format("File {} not treated (not a command)", key))
print(str.format("Number of command(s) : {} / Average command price : {} / Sales revenue : {}", str(commands), str(price/commands), str(price)))