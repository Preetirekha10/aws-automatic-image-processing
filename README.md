# Automated Image Processing using AWS

## Project Overview

This project demonstrates a serverless image processing workflow using AWS S3, AWS Lambda, Python, Pillow, IAM, and Amazon CloudWatch.

When an image is uploaded to the S3 `input/` folder, an S3 event automatically triggers the Lambda function. The Lambda function uses Pillow to resize the image and saves the processed image to the `output/` folder.

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch

## Technologies

- Python
- Pillow
- AWS

## Workflow

1. User uploads an image to the S3 `input/` folder.
2. Amazon S3 generates an object-created event.
3. The event triggers the Lambda function.
4. Lambda downloads the image from S3.
5. Pillow processes and resizes the image.
6. Lambda uploads the processed image to the S3 `output/` folder.
7. CloudWatch stores Lambda execution logs.

## Image Processing

The Lambda function resizes images while maintaining their aspect ratio.

**Maximum dimensions:** `800 x 800`

## Project Structure

```text
aws-automatic-image-processing/
├── README.md
├── lambda_function.py
├── architecture.jpeg
└── screenshots/
    ├── 01-s3-bucket.png
    ├── 02-lambda-overview-and-s3-trigger.png
    ├── 03-pillow-layer.png
    ├── 04-input-image.png
    ├── 05-cloudwatch-logs.png
    └── 06-output-image.png

## Testing

A test image named `test.jpg` was uploaded to the S3 `input/` folder. The S3 event automatically triggered the Lambda function, which processed and resized the image. The processed image was successfully stored in the S3 `output/` folder.

## Monitoring

Amazon CloudWatch Logs were used to monitor Lambda execution and verify successful image processing.

## Skills Demonstrated

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- Python
- Pillow
- Serverless Architecture
- Event-Driven Architecture
