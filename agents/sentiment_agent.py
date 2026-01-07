from transformers import pipeline

class SentimentAgent:
    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def run(self, text):
        res = self.model(text)[0]
        return {"sentiment": res["label"], "confidence": float(res["score"])}
