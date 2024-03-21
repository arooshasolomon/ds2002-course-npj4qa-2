import boto3
import urllib.request 

#Download file from URL and save locally
url= input("Enter URL of the file you want to download: ")
file_name = input("Enter the name to save the file as: ")
urllib.request.urlretrieve(url, file_name)

#Upload file to s3 bucket
bucket_name = input("Enter the name of your s3 bucket: ")
object_name = input("Enter the name to save the file as in s3: ")
s3= boto3.client('s3')
s3.upload_file(file_name, bucket_name, object_name)

expires_in= 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", response)
