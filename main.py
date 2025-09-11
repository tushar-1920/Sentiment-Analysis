from flask import Flask, render_template, request
from textblob import TextBlob
gtthrthtr
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    analysis = None
    if request.method == "POST":
        user_text = request.form["user_text"]
        blob = TextBlob(user_text)

        # Polarity (-1 to 1), Subjectivity (0 to 1)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Classify based on polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        analysis = {
            "text": user_text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment
        }

    return render_template("index.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
