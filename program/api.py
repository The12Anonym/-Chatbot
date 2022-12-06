import openai
import constants as c

ApiModel=c.MODELS[c.MODEL_CHOSEN]

def openApiCall(convo):
    response = openai.Completion.create(
        model=ApiModel,
        prompt=convo,
        temperature=c.MODEL_TEMPERATURE,
        max_tokens=c.MODEL_MAX_TOKENS,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["B:"])
    return response

def getText(openAiObject):
    if (len(openAiObject.choices) == 1):
        text = openAiObject.choices[0].text
    else:
        #find best choice 
        print("Number of answers:" + str(len(openAiObject.choices)))
        text = openAiObject.choices[0].text

    return text
