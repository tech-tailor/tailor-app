from django.test import TestCase
import boto3
from botocore.exceptions import NoCredentialsError

def delete_s3_files(s3_object_key):
    s3_bucket_name = 'tailorapp-app-storage'

    print('s3_bucket_name: {}'.format(s3_bucket_name))
    print('s3_object_key: {}'.format(s3_object_key))
            
    try:
        s3_client = boto.client('s3')
        s3_client.delete_object(Bucket=s3_bucket_name, key=s3_object_key)

    except NoCredentialsError:
        print('no credentials found')

delete_s3_files('asdfg.jpg')
