// Amazon Titan models	Image resolution	Price per image generated for Standard quality	Price per image generated for Premium quality
// Amazon Titan Image Generator v1	Smaller than 512 x 512	$0.01	$0.012
// Amazon Titan Image Generator v1	Larger than 512 x 512	$0.012	$0.014

{
 "modelId": "amazon.titan-image-generator-v1",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"textToImageParams\":{\"text\":\"this is where you place your input text\"},\"taskType\":\"TEXT_IMAGE\",\"imageGenerationConfig\":{\"cfgScale\":8,\"seed\":42,\"quality\":\"standard\",\"width\":1024,\"height\":1024,\"numberOfImages\":3}}"
}

// Scenario 2: Large request LLama3
// Input: 5,000 tokens( 1 token ≈ 4 characters (including spaces & punctuation))
// Output: 10,000 tokens
// Total Cost:
// Input cost: (5,000 ÷ 1,000) × $0.00036 = $0.0018
// Output cost: (10,000 ÷ 1,000) × $0.00072 = $0.0072
// Total cost for this request: $0.009 (≈ 0.9 cents)
// Key Takeaways:
// The more text you send or generate, the higher the cost.
// The output is twice as expensive as the input.


// #Enable IAM Identity Center to make UI for organisation 
// #https://d-9f67788b37.awsapps.com/start 
// #aws sts get-session-token --duration-seconds 3600


// awsbedrockuser
// aws configure sso
// url:https://861276092329.signin.aws.amazon.com/console

// aws sso-oidc start-device-authorization --client-id "" --client-secret "" --start-url https://d-9f67788b37.awsapps.com/start

// your-client-id and your-client-secret


#go to iam console to create user and create access key


Purchased LLama3:8B instruct to work
#Llama 3 8B Instruct


{
 "modelId": "meta.llama3-8b-instruct-v1:0",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
}

#Sold by: Meta
#Categories: Text summarization, Text classification, Sentiment analysis
#Deployment type: Serverless 

#create virtual env 
pwd
/Users/dushyantsharma/Desktop/awsfreetier/awsbedrock
python3 -m venv /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv (make a virutal env)
source /Users/dushyantsharma/Desktop/awsfreetier/awsbedrock/venv/bin/activate (activate virutal env)

pip install -r requirements.txt 
