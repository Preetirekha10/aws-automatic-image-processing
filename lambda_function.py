import boto3
from PIL import Image
from io import BytesIO
import urllib.parse

s3 = boto3.client("s3")


def lambda_handler(event, context):

    # Get bucket name
    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    # Get uploaded file name
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    print(f"Processing: {key}")

    # Download image from S3
    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    image_data = response["Body"].read()

    # Open image using Pillow
    image = Image.open(BytesIO(image_data))

    print(f"Original size: {image.size}")

    # Resize image while maintaining aspect ratio
    image.thumbnail((800, 800))

    print(f"New size: {image.size}")

    # Save processed image in memory
    output_buffer = BytesIO()

    image.save(
        output_buffer,
        format=image.format
    )

    output_buffer.seek(0)

    # Change input/ to output/
    output_key = key.replace("input/", "output/", 1)

    # Upload processed image
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=output_buffer,
        ContentType=response.get("ContentType", "image/jpeg")
    )

    print(f"Processed image saved to: {output_key}")

    return {
        "statusCode": 200,
        "body": "Image processed successfully"
    }