import openai
import constants as c
import program.api as api

openai.api_key = c.OPEN_API_KEY
name = c.NAME
prompt = ""

userPrompts = []
botPrompts = []

if (c.MODEL_STARTS_CONVO):   
    print("Hello, how are you?")
    botPrompts.append()

while (prompt != "exit"):
    prompt = input()
    openAiObject = api.openApiCall(prompt)
    print(api.getText(openAiObject))