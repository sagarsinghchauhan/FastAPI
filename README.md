# FastAPI

This repo is for learning FastAPI implementation end to end and getting industry-level experience.

## Topics Covered

### 1. FastAPI Basics
- **main.py** - Patient Management System API with path parameters, query parameters, and error handling

### 2. Pydantic
- **1.pydantic_course.py** - Pydantic basics: BaseModel, Field, type annotations
- **2.Field_validator.py** - Field validators for custom validation logic
- **3.model_validator.py** - Model-level validators
- **4.computed_field.py** - Computed/derived fields
- **5.nested_models.py** - Nested Pydantic models
- **6.serilization.py** - Model serialization and deserialization

### 3. CRUD Operations
- **3.post_request/** - Complete CRUD operations with FastAPI

### 4. ML Model with FastAPI
- **4.ml_model/** - ML model integration with FastAPI and Streamlit frontend
  - `main.py` - FastAPI endpoint serving RandomForest insurance premium predictor
  - `frontend.py` - Streamlit UI for interacting with the prediction API
  - `model.pkl` - Trained RandomForest model

### 5. Industry-Grade Insurance Prediction API
- **5.Insurance_Prediction_/** - Production-ready project with modular structure
  - `app.py` - FastAPI app with health check and prediction endpoints
  - `schema/` - Pydantic models for input validation and response schema
  - `model/` - ML model loading and prediction logic
  - `config/` - Configuration (city tier mapping)
  - `Dockerfile` - Docker containerization for deployment
  - `requirements.txt` - Project dependencies

## Skills Learned

| Skill | Description |
|-------|-------------|
| FastAPI | Building REST APIs with path/query parameters, error handling |
| Pydantic | Data validation, serialization, computed fields, nested models |
| CRUD | Create, Read, Update, Delete operations |
| ML + API | Serving ML models (RandomForest) through API endpoints |
| Streamlit | Building frontend UI for API interaction |
| Project Structure | Modular code with separate schema, model, config layers |
| Response Models | Typed API responses using Pydantic response models |
| Health Checks | API health/status endpoints for monitoring |
| Docker | Containerizing FastAPI apps with Dockerfile and .dockerignore |
| Docker Hub | Building, tagging, and pushing images to Docker Hub |
| Pickle + Sklearn | Loading and serving scikit-learn models via pickle |

## Setup

```bash
pip install fastapi uvicorn pydantic[email] scikit-learn pandas streamlit requests
uvicorn main:app --reload
```

## Docker

```bash
cd 5.Insurance_Prediction_
docker build -t insurance-api .
docker run -p 8000:8000 insurance-api
```
