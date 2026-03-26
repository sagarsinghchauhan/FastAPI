from pydantic import BaseModel , Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category : str  = Field(
        ...,
        description='The predicted insurance premium category',
        example='High'
    )
    confidence : float  = Field(
        ...,
        description="model's confidence score for the predicted class (range : 0 to 1 )",
        example = 0.8432
    )
    class_probalities : Dict[str,float]  = Field(
        ...,
        description= 'Probalitiy distrubution across all possible classes',
        example = {"low":0.01,
                   "Medium":0.15,
                   "HIgh":0.84
                    }
    )