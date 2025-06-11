import os
import requests


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

user_input = input("Whats your Question ? ")
request_body_dict = {
  "contents": [
    {
      "parts": [
        {
          "text": user_input
        }
      ]
    }
  ]
}

response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}", 
                         json=request_body_dict,
                         headers={"Content-Type": "application/json"})
res_dict = response.json()

"""
{'candidates': [{'content': {'parts': [{'text': 'AI learns from data to make predictions or decisions.\n'}], 'role': 'model'}, 'finishReason': 'STOP', 'avgLogprobs': -0.06665009802038019}], 'usageMetadata': {'promptTokenCount': 8, 'candidatesTokenCount': 11, 'totalTokenCount': 19, 'promptTokensDetails': [{'modality': 'TEXT', 'tokenCount': 8}], 'candidatesTokensDetails': [{'modality': 'TEXT', 'tokenCount': 11}]}, 'modelVersion': 'gemini-2.0-flash', 'responseId': 'ehxJaIXlDPr3_NUPucOfkAg'}
"""
print(res_dict["candidates"][0]['content']['parts'][0]['text'])