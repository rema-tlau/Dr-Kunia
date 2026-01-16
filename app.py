from flask import Flask, render_template, request
from healthcare_chatbot import chatbot_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_reply = ""

    if request.method == "POST":
        user_input = request.form["message"]
        age_group = request.form.get("age", "adult")

        bot_reply = chatbot_response(user_input, age_group)

    return render_template(
        "index.html",
        user_input=user_input,
        bot_reply=bot_reply
    )

if __name__ == "__main__":
    app.run(debug=True)
