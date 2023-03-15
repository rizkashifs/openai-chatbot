import json
import openai
import os
# replace path below to certificate
#os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/kasaiyed/Desktop/chatgpt-api/certificate.crt'

try:
    with open("openaikey.json") as jsonfile:
        key = json.load(jsonfile)['key']
        print ('OpenAI Key successfully loaded .. ')
    
except:
    print ("Error! Correct OPENAI API Key please ... ")

# Set API key    
openai.api_key = key

messages = [
    # system message first, it helps set the behaviour of the assistant
    {"role" : "system" , "content": "You are a helpful assistant."},
]

while True:
    #os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/kasaiyed/Desktop/chatgpt-api/certificate.crt'
    message = input ("😃: ")
    if message:
        messages.append(
            { "role": "user" , "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )
    reply = chat_completion.choices[0].message.content
    print(f"🙏: {reply}")
    messages.append({"role": "assistant", "content" : reply})    