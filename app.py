from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

POSITIVE = {
    "love", "great", "excellent", "amazing", "wonderful",
    "good", "happy", "fantastic", "awesome", "best", "like"
}

NEGATIVE = {
    "hate", "terrible", "awful", "bad", "worst",
    "sad", "angry", "horrible", "poor", "disappointed"
}

@app.post("/sentiment")
def sentiment(req: SentimentRequest):
    results = []

    for sentence in req.sentences:
        text = sentence.lower()

        pos = sum(word in text for word in POSITIVE)
        neg = sum(word in text for word in NEGATIVE)

        if pos > neg:
            label = "happy"
        elif neg > pos:
            label = "sad"
        else:
            label = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": label
        })

    return {"results": results}