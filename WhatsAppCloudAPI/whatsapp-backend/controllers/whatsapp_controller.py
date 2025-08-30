import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID=os.getenv("PHONE_NUMBER_ID")

def send_whatsapp_message(number,message):
    url=f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type":"application/json"
    }
    
    payload={
        "messaging_product":"whatsapp",
        "to":number,
        "type":"text",
        "text":{"body":message}
    }
    
    response=requests.post(url,headers=headers,json=payload)
    print("DEBUG RESPONSE:", response.status_code, response.text) 
    try:
        return response.json()
    except Exception as e:
        return {"ERROR":str(e)}