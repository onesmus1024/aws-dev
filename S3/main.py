import boto3


class S3:
    def __init__(self):
        self.s3 = boto3.resource('s3')
    
    def _get_all_buckets_names(self):
        return [bucket.name for bucket in self.s3.buckets.all()]
    def list_buckets(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)
    def create_bucket(self, bucket_name):
        try:
            if bucket_name in self._get_all_buckets_names():
                print('Bucket already exists')
                return
            self.s3.create_bucket(Bucket=bucket_name)
        except Exception as e:
            raise e


    def delete_bucket(self, bucket_name):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            self.s3.Bucket(bucket_name).delete()
        except Exception as e:
            raise e

    def upload_file(self, bucket_name, file_name):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            self.s3.Bucket(bucket_name).upload_file(file_name, file_name)
        except Exception as e:
            raise e
        
    
    def download_file(self, bucket_name, file_name):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            self.s3.Bucket(bucket_name).download_file(file_name, file_name)
        except Exception as e:
            raise e

    def delete_file(self, bucket_name, file_name):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            self.s3.Object(bucket_name, file_name).delete()
        except Exception as e:
            raise e

    def list_files(self, bucket_name):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            for obj in self.s3.Bucket(bucket_name).objects.all():
                print(obj.key)
        except Exception as e:
            raise e

    def list_files_with_prefix(self, bucket_name, prefix):
        try:
            if bucket_name not in self._get_all_buckets_names():
                print('Bucket does not exist')
                return
            for obj in self.s3.Bucket(bucket_name).objects.filter(Prefix=prefix):
                print(obj.key)
        except Exception as e:
            raise e
    

        


if __name__ == '__main__':
    
    try:
        s3 = S3()
        s3.list_buckets()
        print('='*50)
        print('Creating bucket')
        s3.create_bucket('my-bucketh')
        print('='*50)
        print('Listing buckets after creating bucket')
        s3.list_buckets()
        print('='*50)
        print('Deleting bucket')
        s3.delete_bucket('my-bucket')
        print('='*50)
        print('Listing buckets after deleting bucket')
        s3.list_buckets()
        print('='*50)
        print('uploading file to bucket')
        s3.upload_file('my-bucket', 'main.py')
        print('='*50)
        print('Listing files in bucket after uploading file')
        s3.list_files('my-bucket')

        print('='*50)
        print('Downloading file from bucket')
        s3.download_file('my-bucket', 'main.py')
        print('='*50)
        print("deleting file from bucket")
        s3.delete_file('my-bucket', 'main.py')
        print('='*50)
        print('Listing files in bucket after deleting file')
        s3.list_files('my-bucket')
        print('='*50)
        print('uploading file to bucket')
        s3.upload_file('my-bucket', 'main.py')
        print('='*50)
        print('Listing files in bucket after uploading file and checking with prefix')
        s3.list_files_with_prefix('my-bucket', 'm')
        print('='*50)
        print('Deleting file from bucket')
        s3.delete_file('my-bucket', 'main.py')
        print('='*50)
        print('Listing files in bucket after deleting file')
        s3.list_files('my-bucket')
        print('='*50)
        print('Deleting bucket')
        s3.delete_bucket('my-bucket')
        print('='*50)
        print('Listing buckets after deleting bucket')
        s3.list_buckets()

    except Exception as e:
        print(e)


    




