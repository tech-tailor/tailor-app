import os
import boto3
from botocore.exceptions import NoCredentialsError
from decouple import config



def del_s3(s3_object_key):
    
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

    print(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_ENDPOINT_URL )

    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_S3_ENDPOINT_URL)
    bucket_name = 'tailor-app-storage'

    try:

        print(s3_client)

        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print('yes contents')
            for obj in response['Contents']:
                print(f'Object Key: {obj["Key"]}')
        else:
            print('No contents')

        s3_client.delete_object(Bucket=bucket_name, Key=s3_object_key)
        print('S3 object deleted successfully')
    except NoCredentialsError as e:
        print(f'No credentials found, {e}')

del_s3('work/fabric_images/for_insta.jpg')

