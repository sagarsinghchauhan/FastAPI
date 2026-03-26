# FastAPI

This repo is for learning FastAPI implementation end to end and getting industry-level experience.

## Topics Covered

### FastAPI Basics
- **main.py** - Patient Management System API with path parameters, query parameters, and error handling

### Pydantic
- **1.pydantic_course.py** - Pydantic basics: BaseModel, Field, type annotations
- **2.Field_validator.py** - Field validators for custom validation logic
- **3.model_validator.py** - Model-level validators
- **4.computed_field.py** - Computed/derived fields
- **5.nested_models.py** - Nested Pydantic models
- **6.serilization.py** - Model serialization and deserialization

### CRUD Operations
- **3.post_request/** - Complete CRUD operations with FastAPI

### ML Model with FastAPI
- **4.ml_model/** - ML model integration with FastAPI and Streamlit frontend
  - `main.py` - FastAPI endpoint serving RandomForest insurance premium predictor
  - `frontend.py` - Streamlit UI for interacting with the prediction API
  - `model.pkl` - Trained RandomForest model

### Industry-Grade Insurance Prediction API
- **5.Insurance_Prediction_/** - Production-ready project with modular structure
  - `app.py` - FastAPI app with health check and prediction endpoints
  - `schema/` - Pydantic models for input validation and response schema
  - `model/` - ML model loading and prediction logic
  - `config/` - Configuration (city tier mapping)

## Setup

```bash
pip install fastapi uvicorn pydantic[email] scikit-learn pandas streamlit requests
uvicorn main:app --reload
```
