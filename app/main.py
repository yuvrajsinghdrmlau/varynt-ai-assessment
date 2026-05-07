from fastapi import FastAPI
from pydantic import BaseModel

from app.lead_classifier import classify_lead
from app.response_generator import generate_response
from app.provider_router import route_request
from app.vector_search import search_similar_text
app = FastAPI()

class LeadInput(BaseModel):
    name: str
    company: str
    budget: str
    timeline: str
    message: str


@app.post("/classify-lead")
def classify(data: LeadInput):

    result = classify_lead(data.dict())

    response = generate_response(data.dict(), result)

    return {
        "classification": result,
        "response": response
    }


@app.get("/route-ai/{task}")
def route_ai(task: str):

    return route_request(task)


@app.get("/similarity-search/")
def similarity(query: str):

    return search_similar_text(query)
