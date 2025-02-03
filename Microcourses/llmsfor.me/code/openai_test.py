# Make a request to the OpenAI API and return the result
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

completion = client.chat.completions.create(
  model="llama3.2",
  messages=[
    {"role": "user", "content": "Who are you and who made you?"}
  ]
)

print(completion.choices[0].message.content)