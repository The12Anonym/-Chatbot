import openai

openai.api_key = "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"

prompt = "What is your name?"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)