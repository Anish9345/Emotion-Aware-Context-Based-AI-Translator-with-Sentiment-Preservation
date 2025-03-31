from textblob import TextBlob

def detect_sentiment(text):
    """
    Detects the sentiment of the given text.
    Returns: 'positive', 'negative', or 'neutral'.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

# Test the function
if __name__ == "__main__":
    text = input("Enter a sentence: ")
    sentiment = detect_sentiment(text)
    print(f"Sentiment: {sentiment}")