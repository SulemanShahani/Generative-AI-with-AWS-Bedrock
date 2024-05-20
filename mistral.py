import boto3
import json

# Define the prompt
prompt_data = "Act as Shakespeare and write a poem on Generative AI"

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Define the payload with the correct structure
payload = {
    "prompt": f"<s>[INST] {prompt_data} [/INST]",
    "max_tokens": 200,
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50
}

# Convert the payload to JSON format
body = json.dumps(payload)
model_id = "mistral.mistral-7b-instruct-v0:2"

try:
    # Invoke the model
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json",
    )

    # Read and decode the response body
    response_body = response['body'].read().decode('utf-8')
    response_body = json.loads(response_body)
    
    # Print the full response body for debugging
    print("Full Response Body:", json.dumps(response_body, indent=4))

    # Extract the generated text from the response
    outputs = response_body.get("outputs")
    if outputs and len(outputs) > 0:
        response_text = outputs[0].get("text")
        print("Generated Text:", response_text)
    else:
        print("No completions found in the response.")
except Exception as e:
    print("An error occurred:", e)
