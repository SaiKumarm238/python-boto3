import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('users')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
# print(table.creation_date_time)


# # Crating a new item 

# table.put_item(
#    Item={
#         'username': 'saikumar',
#         'first_name': 'Sai',
#         'last_name': 'Kumar',
#         'age': 28,
#         'account_type': 'standard_user',
#     }
# )


# # Getting an item

# response = table.get_item(
#     Key={
#         "username": "saikumar",
#         "last_name": "Kumar"
#     }
# )

# print(response)
# item = response["Item"]
# print(item)


# # Updating an item 

# table.update_item(
#     Key={
#         'username': 'saikumar',
#         'last_name': 'Kumar'
#     },
#     UpdateExpression='SET age = :val1',
#     ExpressionAttributeValues={
#         ':val1': 27
#     }
# )


# response = table.get_item(
#     Key={
#         "username": "saikumar",
#         "last_name": "Kumar"
#     }
# )
# item = response["Item"]
# print(item)


# # Deleting an item

# table.delete_item(
#     Key={
#         "username": "saikumar",
#         "last_name": "Kumar"
#     }
# )

# print("Deleting an item Done")


# Deleting a table

# table.delete()
# print("Table Deleted")