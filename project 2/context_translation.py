from googletrans import Translator
from sentiment_analysis import detect_sentiment  # Import sentiment function

def translate_text(text, target_language):
    """
    Translates text to the target language while preserving sentiment.
    """
    sentiment = detect_sentiment(text)  # Detect sentiment before translation
    
    translator = Translator()
    
    try:
        translated_text = translator.translate(text, dest=target_language).text
        return f"Original Sentiment: {sentiment}\nTranslated Text: {translated_text}"
    except Exception as e:
        return f"Translation Error: {e}"

# Test the function
if __name__ == "__main__":
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")
    
    result = translate_text(text, target_lang)
    print(result)
