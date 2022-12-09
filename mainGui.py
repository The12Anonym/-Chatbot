import openai
import constants as c
import program.api as api
import program.conversation as conv
import PySimpleGUI as sg

openai.api_key = c.OPEN_API_KEY

userPromt = ""

userPrompts = []
botPrompts = []

layout = [
    [sg.Text("This is a Chatbot Project", font='Any 18')], 
    [sg.Multiline(c.MODEL_STARTING_PROMPT, size=(80,20), key='ML1', disabled=True)],
    [sg.Text("Prompt: "), sg.Input(key='INPUT')],
    [sg.Button('Enter', visible=False, bind_return_key=True)],
    [sg.Push(), sg.Button("Enter"), sg.Button("Close")]]

# Create the window
window = sg.Window("Chatbot", layout)

output = ""

if (c.MODEL_STARTS_CONVO):   
    botPrompts.append(c.MODEL_STARTING_PROMPT)
    output += c.MODEL_STARTING_PROMPT + "\n"

# Create an event loop
while True:
    event, values = window.read()

    # presses the OK button
    if event == "Enter":
        
        userPromt = values['INPUT']   
        output += userPromt + "\n"

        window['INPUT'].update('')
        window['ML1'].update(output)
        window.refresh()

        userPrompts.append(userPromt)
        prompt = conv.CreateConvoString(userPrompts, botPrompts)

        botPromptObject = api.openApiCall(prompt)
        botPromt = api.getText(botPromptObject)

        output += botPromt + "\n"
        window['ML1'].update(output)

        botPrompts.append(botPromt)

    # End program if user closes window or
    if event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()
