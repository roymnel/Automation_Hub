from textblob import TextBlob
import json
import os

COPY_FILE = os.path.join("behavioral", "copy_variants.json")

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # -1 (negative) to +1 (positive)

def recommend_headlines():
    with open(COPY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    recommendations = {}

    for page, variants in data.items():
        best_line = None
        best_score = float("-inf")

        for variant in variants:
            score = analyze_sentiment(variant)
            if score > best_score:
                best_score = score
                best_line = variant

        recommendations[page] = {
            "recommended": best_line,
            "score": round(best_score, 3)
        }

    return recommendations

if __name__ == "__main__":
    results = recommend_headlines()
    print("🧠 Sentiment-Optimized Headlines:")
    for page, result in results.items():
        print(f"🔹 {page}: {result['recommended']} (Score: {result['score']})")
