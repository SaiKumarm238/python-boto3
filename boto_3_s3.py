import boto3

# let's use AWS S3
s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
# data = open("eat_sleep_create_repeat.jpg", "rb")
# s3.Bucket("saikumars-bucket").put_object(Key="eat_sleep_create_repeat.jpg", Body=data)