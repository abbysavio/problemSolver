import sys
import requests
import json

//add key
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

with open(sys.argv[1], 'r') as f:
    code = f.read()

prompt = f"""
You're a code optimizer. Analyze this C++ LeetCode solution and:
- Estimate its time and space complexity
- Suggest more efficient approaches if possible
- Output better code if you can

Here is the code:
{code}
"""

res = requests.post(
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}",
    headers={"Content-Type": "application/json"},
    json={
        "contents": [{"parts": [{"text": prompt}]}]
    }
)

response = res.json()
try:
    reply = response["candidates"][0]["content"]["parts"][0]["text"]
    print("\n🧠 Gemini Optimization Report:\n")
    print(reply)
except Exception as e:
    print("Failed to parse response:", e)
    print(json.dumps(response, indent=2))
