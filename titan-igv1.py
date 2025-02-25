#https://ap-south-1.console.aws.amazon.com/bedrock/home?region=ap-south-1#/model-catalog/serverless/amazon.titan-image-generator-v1
#API request
#Sample Json
# {
#  "modelId": "amazon.titan-image-generator-v1",
#  "contentType": "application/json",
#  "accept": "application/json",
#  "body": "{\"textToImageParams\":{\"text\":\"this is where you place your input text\"},\"taskType\":\"TEXT_IMAGE\",\"imageGenerationConfig\":{\"cfgScale\":8,\"seed\":42,\"quality\":\"standard\",\"width\":1024,\"height\":1024,\"numberOfImages\":3}}"
# }

import boto3
import json
import base64
import os
from PIL import Image
from io import BytesIO
from datetime import datetime

bedrock = boto3.client(service_name="bedrock-runtime")
prompt_text = "Provide me a HD image of a man with his dog & travel bike, enjoying sunset near mountains and a blue lake"



# Construct the payload as per the model's requirements
payload = {
    "textToImageParams": {
        "text": prompt_text
    },
    "taskType": "TEXT_IMAGE",
    "imageGenerationConfig": {
        "cfgScale": 10,
        "seed": 0,
        "quality": "standard",  # Options: 'standard', 'high', 'ultra'
        "width": 512,
        "height": 512,
        "numberOfImages": 2
    }
}

body = json.dumps(payload)

model_id = "amazon.titan-image-generator-v1"

#API CALL
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)


response_body = json.loads(response.get("body").read())

print("Keys in response_body:", response_body.keys())


# Define the output file path
output_file = 'response_body.json'

# Write the JSON data to the file
with open(output_file, 'w') as file:
    json.dump(response_body, file, indent=4)



# Extract images from response
images = response_body.get("images", [])

if not isinstance(images, list):
    print("'images' key is not a list.")
else:
    os.makedirs("output", exist_ok=True)  # Ensure output directory exists
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Unique timestamp

    for idx, img_data in enumerate(images):
        if not isinstance(img_data, str):
            print(f"Image data at index {idx} is not a valid base64 string.")
            continue

        try:
            image = Image.open(BytesIO(base64.b64decode(img_data)))
            file_name = f"output/generated_image_{timestamp}_{idx + 1}.png"
            image.save(file_name)
            print(f"Image saved as {file_name}")
        except Exception as e:
            print(f"Failed to process image at index {idx}: {e}")