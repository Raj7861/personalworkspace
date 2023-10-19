from google.cloud import storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/siraj.motaung/personalworkspace/gcp/credentials.json"

def create_bucket(bucket_name, storage_class='STANDARD', location='us-central'):
    storage_client = storage.Client()
    
    bucket = storage_client.create_bucket(bucket_name, location=location)
    
    bucket.storage_class = storage_class
    
    
    
    return f'Bucket {bucket.name} successfully created.'
    
print(create_bucket('test_demo_storage_bucket', 'STANDARD', 'us-central1'))