import json
import boto3

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('challenge_DB')
    # response = {
    #         'headers': {
    #             'Content-Type': 'application/json',
    #             'Access-Control-Allow-Origin': '*'
    #         }
    # }

    if str(event['routeKey']) == "GET /items/{id}":
        item_id = event['pathParameters']['id']
        result = table.get_item(
            Key = {
                'id':item_id
            },
        )
        # reponse['body'] = result['Item']

        visitors = result['Item']['visitors']
        return {
            'statusCode': 200,
            'body': json.dumps(int(visitors)),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    elif  event['routeKey'] == 'PUT /items':
        request_body = json.loads(event['body'])
        #Put item in DynamoDB
        result = table.put_item(
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
