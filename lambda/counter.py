
import os
import json
import boto3
from botocore.exceptions import ClientError

TABLE_NAME = os.getenv("TABLE_NAME", "resume-visitors")
ITEM_ID    = os.getenv("ITEM_ID", "visitorCount")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        resp = table.update_item(
            Key={"id": ITEM_ID},
            UpdateExpression="ADD visits :inc",
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW",
        )
        visits = int(resp["Attributes"]["visits"])
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": str(visits),
        }
    except ClientError as e:
        print(f"DynamoDB error: {e}")
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "internal"}),
        }
