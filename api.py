import openai
import constants as c

def openApiCall(prompt):
    #response = openai.Completion.create(
        #engine=c.MODEL, 
       #prompt=prompt, 
       # temperature=0, #0=no risk, 1=full confident
       # max_tokens=100)
    response = openai.Completion.create(
        model=c.MODEL,
        prompt="You: Hello\nFriend: How are you?.\nYou: Good, and you?\nFriend:",
        temperature=0.5,
        max_tokens=60,
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
