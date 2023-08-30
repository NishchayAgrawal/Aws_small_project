import json
import pandas as pd
import urllib.parse
import awswrangler as wr


def lambda_handler(event, context):
    # Get the bucket and object information from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    # Read the JSON data from S3
    df = wr.s3.read_json(f"s3://{source_bucket}/{source_key}")
    
    # Perform a simple data transformation
    df_step_1 = pd.json_normalize(df['items'])
    
    df = df_step_1.to_dict(orient='records')
    
    # Write the transformed data back to S3
    destination_bucket = 'destination-bucket-name'
    destination_key = f"transformed/{source_key}"
    # wr.s3.to_json(df, f"s3://{destination_bucket}/{destination_key}")
    
     # Convert the transformed data to a JSON string
    transformed_data_json = json.dumps(df)
    
    # Write the JSON string to S3
    wr.s3.to_text(transformed_data_json, f"s3://{destination_bucket}/{destination_key}")
    
    
    return {
        'statusCode': 200,
        'body': 'Data transformation and upload complete'
    }
