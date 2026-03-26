# Monitoring Unencrypted S3 Buckets

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

## Screen Shots
1. Created S3 buckets with and without encryption.
   <img width="1862" height="853" alt="Screenshot 2026-03-25 100358" src="https://github.com/user-attachments/assets/3b68cd5b-d7d5-4012-bb83-cfd3126d4f70" />

2. Enabled encryption (SSE-S3) on one bucket.
   <img width="929" height="476" alt="image" src="https://github.com/user-attachments/assets/9fa34d5a-d8ca-4dde-b064-d73b8ae9b766" />

3. Created IAM role with AmazonS3ReadOnlyAccess.
  <img width="1889" height="874" alt="Screenshot 2026-03-25 100446" src="https://github.com/user-attachments/assets/b8f7bf3f-28e1-4d8d-afdb-249420237195" />

  <img width="1886" height="872" alt="Screenshot 2026-03-25 100434" src="https://github.com/user-attachments/assets/ff74ae36-7d1e-4937-9dfa-77b606435a6d" />

4. Developed Lambda function using Python.
   <img width="1871" height="807" alt="Screenshot 2026-03-25 100319" src="https://github.com/user-attachments/assets/1cfa17b3-2aa3-46d9-b500-23d972016b3c" />

5. Deployed and tested the function.
   <img width="1869" height="859" alt="Screenshot 2026-03-25 100238" src="https://github.com/user-attachments/assets/86973374-687c-42ea-9f8e-718bbbbe02f9" />

6. Verified results in logs.

   <img width="1892" height="878" alt="Screenshot 2026-03-25 100251" src="https://github.com/user-attachments/assets/9f32103e-a8d2-4b1d-bf75-6f5cdf97e05e" />
