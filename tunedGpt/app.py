import json
import os
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError

app = Flask(__name__)
# CHANGE OPENAI_API_KEY -> YOUR_API_KEY
# EXAMPLE 
# openai.api_key = "sk-JUg...."
openai.api_key = "OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [{"role": "user", "content": user_input}]

    try:
        # response = openai.ChatCompletion.create(
        response = openai.Completion.create(
            # model="gpt-3.5-turbo",
            model="davinci:ft-personal:superhero-2023-04-13-01-48-11",
            prompt=user_input
        )
        content = response.choices[0].text
        # content = response.choices[0].message["content"]
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)