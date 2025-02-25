import boto3
import json
#API request
prompt_data="""
Act as a Data Science Interviewer, write 2 important questions with answers you ask while interviewing 3 years experienced data science candidate for a job in your company
"""

#LLama3:8B (Max tokens=8k)

bedrock=boto3.client(service_name="bedrock-runtime", region_name="ap-south-1" )

payload={
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

body=json.dumps(payload)
model_id="meta.llama3-8b-instruct-v1:0"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)
