# Lambda Data Transformation and Create table using AWS Glue Crawler

This AWS Lambda function reads JSON data(raw data) from an S3 bucket, performs data transformation using the Pandas library, and stores the transformed data in Parquet format in another S3 location. The function is triggered whenever a new JSON file is uploaded to the source S3 bucket. Then create table on athena using glue crawler. 


![Architecture](https://github.com/Gaurav0807/Aws_small_project/assets/54076460/264216bb-8700-4f0c-821b-4f1c5b87ccda)



## Table of Contents

- [Functionality](#functionality)
- [Configuration](#configuration)
- [Trigger](#trigger)
- [Usage](#usage)
- [Notes](#notes)

## Functionality

- Reads JSON data from an S3 bucket.
- Uses the Pandas library to transform the JSON data.
- Writes the transformed data to an S3 location in Parquet format.
- Utilizes the AWS Glue Catalog for cataloging the data.

## Configuration

The following environment variables need to be configured for the Lambda function:

- `s3_cleansed_layer`: S3 location where the transformed data will be stored.
- `glue_catalog_db_name`: AWS Glue catalog database name.
- `glue_catalog_table_name`: AWS Glue catalog table name.
- `write_data_operation`: The mode of writing data, e.g., 'overwrite', 'append', etc.

## Trigger

The Lambda function is triggered automatically whenever a new JSON file is uploaded to the source S3 bucket.

## Usage

1. Create an AWS Lambda function.
2. Configure the required environment variables ![env variable](https://github.com/Gaurav0807/Aws_small_project/assets/54076460/e78eb6ff-af15-4f92-964a-6533e7053fd7).
3. Upload the provided code as the function's handler.
4. Add Layer to lambda function (AWSSDKPandas-Python38)
5. Set up the S3 trigger to invoke the Lambda function when a new JSON file is uploaded.


## Notes

- Ensure that necessary AWS IAM permissions are granted to the Lambda function. Permission :- AmazonS3FullAccess, AWSGlueConsoleFullAccess
- The function uses the `awswrangler` library for S3 operations and data transformation.



