from boto3.dynamodb.conditions import Key, Attr
from connect_to_dynamodb import table

#This queries for all of the users whose username key equals saikumar 
response = table.query(
    KeyConditionExpression=Key('username').eq('saikumar')
)
items = response['Items']
print(items)


# similarly you can scan the table based on attributes of the items.
# For example, this scans for all the users whose age is less than 27

response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)