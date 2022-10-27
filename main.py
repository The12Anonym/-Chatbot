import openai
import constants
import ai

openai.api_key = constants.OPEN_API_KEY
name = constants.NAME
prompt = ""

print("Hello my name is " + name)
print ("Please ask me anything")


while (prompt != "exit"):
    prompt = input()
    openAiObject = ai.openApiCall(prompt)
    print(ai.getText(openAiObject))

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)
