import constants as c

def CreateConvoString(userPrompts, botPrompts):
    convo = ""
    i = 0
    for botPromt in botPrompts:
        convo += "b: " + botPromt + "\n"
        convo += "u: " + userPrompts[i] + "\n"
        i += 1
    return convo



        #You: Hello\nFriend: How are you?.\nYou: Good, and you?\nFriend: