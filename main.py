import openai

openai.api_key = "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"

prompt = "Hello world"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)