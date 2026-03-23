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

## Setup

```bash
pip install fastapi uvicorn pydantic[email]
uvicorn main:app --reload
```
