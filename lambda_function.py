import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    buckets = s3.list_buckets()
    unencrypted_buckets = []

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']

        try:
            s3.get_bucket_encryption(Bucket=bucket_name)
        except:
            print(f"Bucket without encryption: {bucket_name}")
            unencrypted_buckets.append(bucket_name)

    if unencrypted_buckets:
        print("Unencrypted Buckets Found:", unencrypted_buckets)
    else:
        print("All buckets are encrypted")

    return {
        'statusCode': 200,
        'unencrypted_buckets': unencrypted_buckets
    }
