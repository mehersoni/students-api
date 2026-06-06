from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    sentences: List[str]

def classify(text: str):
    text = text.lower()

    positive = ["love","great","excellent","amazing","awesome","good","happy","fantastic"]
    negative = ["hate","terrible","awful","bad","worst","sad","horrible","angry"]

    pos = sum(w in text for w in positive)
    neg = sum(w in text for w in negative)

    if pos > neg:
        return "happy"
    elif neg > pos:
        return "sad"
    return "neutral"

@app.post("/")
def sentiment(req: SentimentRequest):
    return {
        "results": [
            {
                "sentence": s,
                "sentiment": classify(s)
            }
            for s in req.sentences
        ]
    }