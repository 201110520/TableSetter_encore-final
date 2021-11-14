import boto3 #pip3 install boto3
import POSvariable

#s3 = boto3.client('s3') #S3에있는 현재 버킷리스트의 정보 가져오기
#response = s3.list_buckets() 
#print(response)



class imageS3Upload:
    def imageUpload(self,Furl):
        s3=boto3.resource('s3',
        aws_access_key_id=POSvariable.s3Variable['ACCESS_KEY_ID'],
        aws_secret_access_key=POSvariable.s3Variable['ACCESS_SECRT_KEY'],
        region_name=POSvariable.s3Variable['region'])

        data = open(Furl,'rb')
        image_name = POSvariable.STORE_ID+'/'+Furl.split('/')[-1]
        #print(mylist)

        s3.Bucket(POSvariable.s3Variable['BUCKET_NAME']).put_object(Body=data,Key=image_name,ContentType='image/png',ACL='public-read')
