from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    sentences: List[str]

@app.post("/sentiment")
def sentiment(req: SentimentRequest):
    positive = {
        "love","great","excellent","amazing","awesome",
        "good","happy","fantastic","wonderful","best"
    }

    negative = {
        "hate","terrible","awful","bad","worst",
        "sad","horrible","angry","disappointed"
    }

    results = []

    for sentence in req.sentences:
        text = sentence.lower()

        pos = sum(word in text for word in positive)
        neg = sum(word in text for word in negative)

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