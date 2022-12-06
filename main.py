import openai
import constants as c
import program.api as api
import program.conversation as conv

openai.api_key = c.OPEN_API_KEY

userPromt = ""

userPrompts = []
botPrompts = []

if (c.MODEL_STARTS_CONVO):   
    print(c.MODEL_STARTING_PROMPT)
    botPrompts.append(c.MODEL_STARTING_PROMPT)

while (userPromt != "exit"):
    userPromt = input()
    userPrompts.append(userPromt)

    prompt = conv.CreateConvoString(userPrompts, botPrompts)

    botPromptObject = api.openApiCall(prompt)
    botPromt = api.getText(botPromptObject)
    print(botPromt)    
    botPrompts.append(botPromt)