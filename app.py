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
  pass
