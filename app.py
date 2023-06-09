from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv



# https://platform.openai.com/account/api-keys