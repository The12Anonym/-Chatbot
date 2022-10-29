import openai
#import json

def openApiCall(prompt):
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)
    return response

def getText(openAiObject):
    if (len(openAiObject.choices) == 1):
        text = openAiObject.choices[0].text
    else:
        #find best choice 
        text = openAiObject.choices[0].text

    return text
