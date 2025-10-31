import openai

openai.api_key = "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"
def chat_with_gpt(promt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content":  promt}]
    )

    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ",response)
