from flask import Flask, render_template, request
from googletrans import Translator
from sentiment_analysis import detect_sentiment  # Import sentiment function

app = Flask(__name__)

def translate_text(text, target_language):
    """
    Translates text to the target language while preserving sentiment.
    """
    sentiment = detect_sentiment(text)  # Detect sentiment before translation
    translator = Translator()
    
    try:
        translated_text = translator.translate(text, dest=target_language).text
        return sentiment, translated_text
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        target_lang = request.form["target_lang"]
        sentiment, translated_text = translate_text(text, target_lang)
        return render_template("index.html", sentiment=sentiment, translated_text=translated_text, original_text=text, target_lang=target_lang)
    return render_template("index.html", sentiment=None, translated_text=None)

if __name__ == "__main__":
    app.run(debug=True)
