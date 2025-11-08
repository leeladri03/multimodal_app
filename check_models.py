import google.generativeai as genai

genai.configure(api_key="AIzaSyD5X-wZ6Nrrqe28WW_tnvFQtraJPMyop4s")

print("\n🔍 Listing available models for this key:\n")
for m in genai.list_models():
    print(m.name)
