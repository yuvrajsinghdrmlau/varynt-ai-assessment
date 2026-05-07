# VARYNT AI Assessment

## Overview
This project demonstrates a simple AI workflow system for KeaBuilder.

Features:
- AI lead classification
- Personalized response generation
- Multi-provider AI routing
- Similarity search using vector embeddings

## Tech Stack
- Python
- FastAPI
- Sentence Transformers
- FAISS

## API Endpoints

### POST /classify-lead
Classifies leads into:
- HOT
- WARM
- COLD

### GET /route-ai/{task}
Routes requests to:
- Image AI
- Video AI
- Voice AI

### GET /similarity-search/
Performs semantic similarity search.

## Run Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
