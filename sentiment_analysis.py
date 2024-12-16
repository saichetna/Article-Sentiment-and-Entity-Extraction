from transformers import pipeline

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # Limit text length to 512 tokens
        sentiment = result['label']
        confidence = result['score']
        return f"{sentiment} (Confidence: {confidence:.2f})"
    except Exception as e:
        return f"Error analyzing sentiment: {str(e)}"
