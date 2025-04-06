import boto3
import json

def query_bedrock_claude(prompt, model_id="anthropic.claude-3-sonnet-20240229-v1:0"):
    bedrock = boto3.client("bedrock-runtime")
    body = {
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.2
    }
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )
    return json.loads(response['body'].read())['completion']
