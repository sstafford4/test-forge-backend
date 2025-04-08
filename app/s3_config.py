import boto3

BUCKET_NAME = "babys-first-bucket-ss-2025"
REGION_NAME = "us-east-2"

s3 = boto3.client("s3", region_name=REGION_NAME)