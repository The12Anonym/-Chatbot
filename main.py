import openai
import constants as c
import api

openai.api_key = c.OPEN_API_KEY
name = c.NAME
prompt = ""

print("Hello my name is " + name)
print("Please ask me anything")

while (prompt != "exit"):
    prompt = input()
    openAiObject = api.openApiCall(prompt)
    print(api.getText(openAiObject))