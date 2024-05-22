import google.generativeai as genai

genai.configure(api_key="AIzaSyD68a2BKMMY_KZMmej-ZBmNVmgYMXr9fSUy")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Qual o sentido da vida?")

print(response.text)
