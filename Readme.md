#create virtual env 
pwd
/Users/dushyantsharma/Desktop/awsfreetier/awsbedrock
python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv (make a virutal env)
source /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv/bin/activate (activate virutal env)

pip install -r requirements.txt 

#go to iam console to create user and create access key


Purchased LLama3:8B instruct to work
#Llama 3 8B Instruct

<!-- 
{
 "modelId": "meta.llama3-8b-instruct-v1:0",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
} -->

#Sold by: Meta
#Categories: Text summarization, Text classification, Sentiment analysis
#Deployment type: Serverless 