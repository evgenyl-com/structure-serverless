import json
import os
import boto3


REGION = os.getenv('REGION', 'us-east-1')
DYNAMODB_RESOURCE = boto3.resource('dynamodb', region_name=REGION)

EXAMPLE_TABLE_NAME = os.getenv('EXAMPLE_TABLE_NAME', 'main-us-east-1-example-shared-billing')
EXAMPLE_TABLE_RESOURCE = DYNAMODB_RESOURCE.Table(EXAMPLE_TABLE_NAME)


def response(code, response):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps(response)
    }


def lambda_handler(event, context):
    payload = json.loads(event['body'])
    claims = event['requestContext']['authorizer']['claims']
    return response(200, claims)


if os.getenv('ENV', 'local') != 'AWS':
    event = {<event>}
    event['body'] = str(event['body'])
    print(lambda_handler(event, 'context'))

