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
#             'Content-Type': 'application/json',
#             'Access-Control-Allow-Origin': '*'
#         }
#     }

#     #Dispatch based on the route key
#     try:
#         if event['httpMethod'] == 'GET':
#             #Get item from DynamoDB

#             result = table.get_item(
#                 Key = {
#                     'id':'1'
#                 },
#                 )
#             reponse['body'] = result['Item']
#         elif event['httpMethod'] == 'PUT':
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
#             raise ValueError(f'Unsupported route: "{event["httpMethod"]}"')

#     except Exception as e:
#         # Set the response status code to 400 (Bad Request) and the body to the error message
#         response['statusCode'] = 400
#         response['body'] = str(e)
#         # Convert the body to a JSON string
#         response['body'] = json.dumps(response['body'])

#     return response

def lambda_handler(event,context):


    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('challenge_DB')

    if str(event['routeKey']) == "GET /items/{id}":
        item_id = event['pathParameters']['id']
        result = table.get_item(
            Key = {
                'id':item_id
            },
        )
        # reponse['body'] = result['Item']
        return {
            'statusCode': 200,
            'body': json.dumps(str(result['Item'])),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    elif  event['routeKey'] == 'PUT /items':
        request_body = json.loads(event['body'])
        #Put item in DynamoDB
        response = table.put_item(
            Item={
                'id' : request_body['id'],
                'visitors' : request_body['visitors']
            })
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps(event['routeKey']),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
