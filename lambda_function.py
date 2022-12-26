import json
import boto3

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
