{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "dda9370d-6454-434e-b13a-b28f74f5c328",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import os\n",
    "from flask import Flask, render_template, request, jsonify\n",
    "import openai\n",
    "from openai.error import RateLimitError\n",
    "\n",
    "app = Flask(__name__)\n",
    "CHANGE OPENAI_API_KEY -> YOUR_API_KEY\n",
    "openai.api_key = 'OPENAI_API_KEY'\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/gpt4', methods=['GET', 'POST'])\n",
    "def gpt4():\n",
    "    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']\n",
    "    messages = [{\"role\": \"user\", \"content\": user_input}]\n",
    "\n",
    "    try:\n",
    "        # response = openai.ChatCompletion.create(\n",
    "        response = openai.Completion.create(\n",
    "            # model=\"gpt-3.5-turbo\",\n",
    "            model=\"davinci:ft-personal:superhero-2023-04-13-01-48-11\",\n",
    "            prompt=user_input\n",
    "        )\n",
    "        content = response.choices[0].text\n",
    "        # content = response.choices[0].message[\"content\"]\n",
    "    except RateLimitError:\n",
    "        content = \"The server is experiencing a high volume of requests. Please try again later.\"\n",
    "\n",
    "    return jsonify(content=content)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
