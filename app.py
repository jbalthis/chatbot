from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv



# https://platform.openai.com/account/api-keys
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# print(openai.api_key)

# Setup Flask app
app = Flask(__name__)


# Define the home page route
@app.route("/")
def Home():
    return render_template("index.html")

# Define Chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # pass
    # get the message input from the user
    user_input = request.form["message"]
    # use the openai API to generate a response
    prompt = f"User: {user_input}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]
    )

    # extract the response etxt from openai api result
    bot_response = response.choices[0].text.strip()

    # add the user input and bot response to the chat history
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    # render the Chatbot template with the response
    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response
    )

# start the flask app
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(port=55000)