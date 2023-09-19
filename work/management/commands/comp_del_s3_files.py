import os
from decouple import config
import boto3
from botocore.exceptions import NoCredentialsError
from django.core.management.base import BaseCommand
from work.models import Jobs, Workers

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

class Command(BaseCommand):
    help = 'Compare files associated with models to specific S3 folders and delete files not in the models'

    def handle(self, *args, **options):
        # Define a list of model classes to compare
        model_classes_to_compare = [Jobs, Workers]

        for model_class in model_classes_to_compare:
            # Get all instances of the model
            instances = model_class.objects.all()

            # Specify the S3 folder for the current model class
         
            if model_class == Jobs:
                s3_folder = 'work/jobs'
            elif model_class == Workers:
                s3_folder = 'worker/profile_pic'
            else:
                # Handle other models or set a default folder
                s3_folder = 'default_folder/'

            # Create a set to store filenames from the model
            model_filenames = set()

            # Populate the set with filenames from the model
            for instance in instances:
                image1 = instance.fabric_image_1
                image2 = instance.fabric_image_2
                image3 = instance.top_design_image_1
                image4 = instance.top_design_image_2
                
                if image1:
                    model_filenames.add(image1.name)
                if image2:
                    model_filenames.add(image2.name)
                if image3:
                    model_filenames.add(image3.name)
                if image4:
                    model_filenames.add(image4.name)

            # Compare model filenames with objects in the specified S3 folder
            s3_bucket_name = 'tailor-app-storage'
            s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=AWS_S3_ENDPOINT_URL)



            try:
                s3_objects = s3_client.list_objects_v2(Bucket='tailor-app-storage', Prefix=s3_folder)
                for s3_object in s3_objects.get('Contents', []):
                    s3_object_key = s3_object['Key']
                    if s3_object_key not in model_filenames:
                        try:
                            # Delete S3 object not in the model
                            s3_client.delete_object(Bucket=s3_bucket_name, Key=s3_object_key)
                            self.stdout.write(self.style.SUCCESS(f"Deleted S3 object: {s3_object_key}"))
                        except NoCredentialsError:
                            self.stderr.write(self.style.ERROR('No AWS credentials found'))    
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error listing S3 objects: #{str(e)}"))
