from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Replace the following with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/prompt', methods=['POST'])
def prompt():
    # Extract the prompt string from the request body
    prompt_str = request.form['prompt']
    print(prompt_str)
    if not prompt_str:
        return "Bad Request", 400

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_str,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the response as a string
    return response["choices"][0]["text"], 200

if __name__ == '__main__':
    app.run()
