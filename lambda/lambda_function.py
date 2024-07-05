import json
import boto3
import os

s3 = boto3.client('s3')
source_bucket = os.environ['SOURCE_BUCKET']
destination_bucket = os.environ['DESTINATION_BUCKET']

def lambda_handler(event, context):
    # Print the event details
    print("Event: ", json.dumps(event, indent=2))
    
    for record in event['Records']:
        # Get the object from the event
        key = record['s3']['object']['key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        
        try:
            # Copy the object to the destination bucket
            s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)
            print(f'Successfully copied {key} from {source_bucket} to {destination_bucket}')
        except Exception as e:
            print(f'Error copying object {key}: {str(e)}')
            raise e
    
    return {
        'statusCode': 200,
        'body': json.dumps('Copy complete')
    }
