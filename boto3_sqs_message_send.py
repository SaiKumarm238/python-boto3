import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = "https://sqs.us-east-1.amazonaws.com/490738608717/TEST_SQS_QUEUE"

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl = queue_url,
    DelaySeconds = 10,
    MessageAttributes = {
        "Title": {
            "DataType": "String",
            "StringValue": "The Assassin"
        },
        "Author": {
            "DataType": "String",
            "StringValue": "Saikumar"
        },
        "WeekOn": {
            "DataType": "Number",
            "StringValue": "10"
        }
    },
    MessageBody=(
        "Information about current NY Times fiction bestseller for "
        "week of 22/05/2023."
    )
)

print(response["MessageId"])