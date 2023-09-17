import os
import boto3
from botocore.exceptions import NoCredentialsError
from decouple import config



def del_s3(s3_object_key):
    
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_S3_ENDPOINT_URL = 'https://s3.us-east-005.backblazeb2.com'

    print(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_ENDPOINT_URL )

    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_S3_ENDPOINT_URL)
    bucket_name = 'tailor-app-storage'

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=s3_object_key)

        response = s3_client.list_objects(Bucket=bucket_name)
        print('S3 object deleted successfully')
        if 'Contents' in response:
            print('yes contents')
            for obj in response['Contents']:
                print(f'Object Key: {obj["Key"]}')
    except NoCredentialsError as e:
        print(f'No credentials found, {e}')

del_s3('work/fabric_images/agbada.jpg')


