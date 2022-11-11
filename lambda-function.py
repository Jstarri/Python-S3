import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    bucket_names = []
    buckets = response["Buckets"]
    
    for bucket in buckets:
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])
        
    return {
        "body": json.dumps(bucket_names)
    }