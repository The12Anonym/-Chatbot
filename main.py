import openai

openai.api_key = "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"

prompt = "What is your name?"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)