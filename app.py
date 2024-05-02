from flask import Flask, render_template, request
import openai
import logging

app = Flask(__name__)

openai.api_key = 'sk-proj-BvLZP4L5XyS2d6YEd5lAT3BlbkFJXQAYQXtUG57ZcVCQNy8g'

logging.basicConfig(level=logging.ERROR)
log = logging.getLogger('werkzeug')
log.disabled = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ["POST"])
def api():
    
    message = request.json.get("message")
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else:
        return 'Cannot generate respinse!'
    
if __name__=='__main__':
    app.run(debug=False)