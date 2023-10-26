import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "Key"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine ="text-davinci-003",
            prompt=user_input,
            max_tokens=3000, # more than 3000 words
            temperature=0.5 # accuracy
        ).choices[0].text
        return  response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write about Paul apostle")
    print(response)
