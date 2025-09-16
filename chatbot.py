import openai

openai.api_key = "YOUR_API_KEY_HERE"  # <-- put your real API key here

print("Welcome to your chatbot! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4o" if your account has access
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response.choices[0].message["content"]
    print("Bot:", reply, "\n")
