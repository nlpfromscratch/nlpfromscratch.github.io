from ollama import chat

response = chat(model="llama3.2",
                messages=[{"role":"user",
                     "content":"Who are you? Answer in 150 paragraphs."}],
                     stream=True
                     )

for chunk in response:
    print(chunk['message']['content'], end="", flush=True)