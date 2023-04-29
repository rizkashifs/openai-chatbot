import json
import openai
import os
import certifi
import ssl
import requests

requests.packages.urllib3.disable_warnings()
# replace path below to certificate
os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/kasaiyed/Documents/GitHub/openai-chatbot/certificate.crt'
ssl_context = ssl.create_default_context(cafile=certifi.where())

if __name__ == "__main__":
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