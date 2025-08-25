import json
import os
import boto3


REGION = os.getenv('REGION', 'us-east-1')
DYNAMODB = boto3.client('dynamodb', region_name=REGION)

EXAMPLE_TABLE_NAME = os.getenv('EXAMPLE_TABLE_NAME', 'example-table-name')


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


def example_func():
    print("This is an example function running as a daily cron job.")
    return True


def lambda_handler(event, context):
    example_func()
    return response(200, {"status": "success"})


if os.getenv('ENV', 'local') != 'AWS':
    event = {<event>}
    event['body'] = str(event['body'])
    print(lambda_handler(event, 'context'))
