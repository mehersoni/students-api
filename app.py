from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from textblob import TextBlob


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    sentences: List[str]



def classify(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
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