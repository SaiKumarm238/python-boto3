import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='TEST_SQS_QUEUE',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)
print(response['QueueUrl'])

# List SQS queues
response = sqs.list_queues()
print(response)

# Get URL for SQS queue
# response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')

# print(response['QueueUrl'])

# Delete SQS queue
# sqs.delete_queue(QueueUrl='SQS_QUEUE_NAME')