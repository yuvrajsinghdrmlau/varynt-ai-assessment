# ML Engineer Assessment Answers

## Q1 - Similarity Matching System

Implemented semantic similarity search using:
- Sentence Transformers
- FAISS

Workflow:
- Convert text into embeddings
- Store vectors in FAISS
- Compare query embedding
- Return top match

Example:
Query: "AI automation"
Top Match: "AI funnel automation"

---

## Q2 - Serving ML Model with Node.js Backend

Architecture:

Node.js Backend
↓
REST API
↓
FastAPI ML Service
↓
ML Model Inference

Reason:
Python ecosystem is better for ML inference while Node.js handles application logic.

---

## Q3 - Database Schema

### users
- id
- name
- email
- created_at

### user_inputs
- id
- user_id
- input_text
- created_at

### predictions
- id
- input_id
- prediction
- confidence_score
- model_version
- created_at

---

## Q4 - Slow ML Responses

Use:
- asynchronous processing
- loading indicators
- polling/WebSockets for status updates

---

## Q5 - Notebook → Production Challenges

1. Dependency mismatch
2. Slow inference
3. Scaling concurrent requests

---

## Q6 - LoRA Face Consistency

Workflow:
- Collect user images
- Train LoRA adapter
- Store LoRA weights
- Use Base Model + LoRA during inference

Benefits:
- Lightweight
- Faster
- Consistent outputs

---

## Q7 - Tools

- Python
- FastAPI
- PyTorch
- OpenCV
- EfficientNet
- HuggingFace
- FAISS
- Git/GitHub
- SQLite/PostgreSQL
