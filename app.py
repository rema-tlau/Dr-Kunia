from flask import Flask, render_template, request
from healthcare_chatbot import chatbot_response
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_reply = ""

    if request.method == "POST":
        user_input = request.form["message"]
        bot_reply = chatbot_response(user_input)

    return render_template(
        "index.html",
        user_input=user_input,
        bot_reply=bot_reply
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
