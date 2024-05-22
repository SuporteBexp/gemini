import google.generativeai as genai

genai.configure(api_key="AIzaSyD68a2BKMMY_KZMmej-ZBmNVmgYMXr9fSU")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("O que tem de novo no Jeep Renegade?", stream=True)

for chunk in response:
    print(chunk.text)
    print("_"*80)
