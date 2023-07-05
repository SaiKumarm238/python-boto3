import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = "https://sqs.us-east-1.amazonaws.com/490738608717/TEST_SQS_QUEUE"

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]

print(f"Received and deleted message: {message}")


# Delete received message from queue
receipt_handle = message['ReceiptHandle']
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
