import constants as c

def CreateConvoString(userPrompts, botPrompts):
    startingPrompts = userPrompts
    secondPrompts = botPrompts

    if (c.MODEL_STARTS_CONVO):
        startingPrompts = botPrompts
        secondPrompts = userPrompts

    convo = "A: "
    i = 0
    for startingPrompt in startingPrompts:
        convo += startingPrompt + "\n"
        convo += "B: " + secondPrompts[i] + "\nA:"
        i += 1
    return convo