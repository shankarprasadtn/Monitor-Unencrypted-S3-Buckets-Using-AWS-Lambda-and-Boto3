# Assignment 3: Monitoring Unencrypted S3 Buckets

## Objective
Detect S3 buckets without server-side encryption using AWS Lambda and Boto3.

## Steps Followed
1. Created S3 buckets with and without encryption.
2. Enabled encryption (SSE-S3) on one bucket.
3. Created IAM role with AmazonS3ReadOnlyAccess.
4. Developed Lambda function using Python.
5. Deployed and tested the function.
6. Verified results in CloudWatch logs.

## Result
The Lambda function successfully identified unencrypted S3 buckets.

## Tools Used
- AWS Lambda
- Amazon S3
- IAM
- Python (Boto3)

## Output
Returns list of unencrypted buckets.
