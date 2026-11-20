# AI Knowledge Assistant

A Python-based backend project for building a reliable, testable AI knowledge assistant.

The project is being developed incrementally, with an emphasis on clean architecture, automated testing, error handling, and reproducible development environments.

## Current Features

- REST API built with FastAPI
- Health check endpoint
- API tests using pytest and FastAPI TestClient
- Reusable test fixtures
- Dependency management with uv

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- pytest
- HTTPX
- uv

## Getting Started

### Prerequisites

Install [uv](https://docs.astral.sh/uv/).

### Installation

Clone the repository and navigate to the project directory.

Install dependencies:

```bash
uv sync
```

### Run the API

```bash
uv run uvicorn ai_knowledge_assistant.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

## Running Tests

```bash
uv run pytest -v
```
The current test suite covers:

| Test Case | Expected Result |
|---|---|
| Health endpoint | HTTP 200 |
| Unknown endpoint | HTTP 404 |
| Unsupported HTTP method | HTTP 405 |
| JSON response content type | application/json |

## Planned Features

- PDF document ingestion
- Text chunking and embeddings
- Vector-based document retrieval
- Retrieval-Augmented Generation (RAG)
- Evaluation datasets
- Failure analysis and error handling
- Reproducible AI evaluation reports

## Engineering Approach

The project follows an incremental development process:

1. Implement a small feature.
2. Define expected behavior.
3. Write automated tests.
4. Identify failure cases.
5. Improve the implementation.
6. Document the results.

## Project Status

**v0.1.0 — Initial FastAPI backend and automated API tests.**

The RAG and LLM components are not yet implemented.