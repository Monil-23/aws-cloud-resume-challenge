import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('resume-challenge')

def lambda_handler(event, context):
    response = table.get_item(Key={'id': '0'})
    views = response.get('Item', {}).get('views', 0)
    views += 1

    table.put_item(Item={'id': '0', 'views': views})

    return {
        'statusCode': 200,
        'body': json.dumps({'views': int(views)})
    }
