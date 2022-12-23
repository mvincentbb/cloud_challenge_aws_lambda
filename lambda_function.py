import json
import boto3

# def lambda_handler(event, context):
#     # TODO implement
#     # return {
#     #     'statusCode': 200,
#     #     'body': json.dumps('Hello from Lambda!')
#     # }

#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('challenge_DB')


#     response = {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         }
#     }

#     #Dispatch based on the route key
#     try:
#         if event['routeKey'] == 'GET /items/{id}':
#             #Get item from DynamoDB

#             result = table.get_item(
#                 Key = {
#                     'id':'1'
#                 },
#                 )
#             reponse['body'] = result['Item']
#         elif event['routeKey'] == 'PUT /items':
#             #Parse the request

#             request_body = json.loads(event['body'])
#             #Put item in DynamoDB
#             table.put_item(
#                 Item={
#                     'id' : event['pathParameters']['id'],
#                     'visitors' : 1
#                 }
#                 )
#             reponse['body'] =  f'Put item '

#         else:
#             raise ValueError(f'Unsupported route: "{event["routeKey"]}"')

# except Exception as e:
#     # Set the response status code to 400 (Bad Request) and the body to the error message
#     response['statusCode'] = 400
#     response['body'] = str(e)
# # Convert the body to a JSON string
# response['body'] = json.dumps(response['body'])

# return result

def lambda_handler(event,context):
    item_id = event['pathParameters']['id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('challenge_DB')
    response = table.get_item(
        Key = {
            'id': "1"
        }
    )
    # statusCode = 200
    # return {
    #     "statusCode": statusCode,
    #     "body": json.dumps(response['Item']),
    #     "headers": {
    #         "Content-Type": "application/json"
    #     }
    body = json.dumps(str(response['Item']))
    return {
        'statusCode': 200,
        'body': body,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
