import os
import sys
from hate.exception import CustomException

class s3Operation:
    def sync_folder_to_s3(self, bucket_name, filepath, filename):
        try:
            command = f"aws s3 cp {filepath}/{filename} s3://{bucket_name}/{filename}"
            os.system(command)
        except Exception as e:
            raise CustomException(e, sys)
        
    def sync_folder_from_s3(self, bucket_name, filename, destination):
        try:
            command = f"aws s3 cp s3://{bucket_name}/{filename} {destination}/{filename}"
            os.system(command)
        except Exception as e:
            raise CustomException(e,sys)