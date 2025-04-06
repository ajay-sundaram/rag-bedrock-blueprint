import boto3
import json

def get_bedrock_embedding(text, model_id="amazon.titan-embed-text-v1"):
    bedrock = boto3.client("bedrock-runtime")
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"inputText": text})
    )
    return json.loads(response['body'].read())['embedding']
