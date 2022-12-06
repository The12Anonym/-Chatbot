import openai
import constants as c

ApiName=c.MODEL_CHOSEN
ApiModel=c.MODELS[ApiName]

def openApiCall(prompt):
    response = openai.Completion.create(
        model=ApiModel,
        prompt="You: Hello\nFriend: How are you?.\nYou: Good, and you?\nFriend:",
        temperature=c.MODEL_TEMPERATURE,
        max_tokens=c.MODEL_MAX_TOKENS,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"])
    return response

def getText(openAiObject):
    if (len(openAiObject.choices) == 1):
        text = openAiObject.choices[0].text
    else:
        #find best choice 
        print("Number of answers:" + str(len(openAiObject.choices)))
        text = openAiObject.choices[0].text

    return text
