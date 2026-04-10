from pydantic import BaseModel, Field
from typing import List, Optional

class ResponseModel(BaseModel):
    healthy: Optional[bool] = Field(None, description="Whether the plant is healthy or not")
    disease: Optional[str] = Field(None, description="The disease name")
    description: Optional[str] = Field(None, description="Description of the disease")
    treatment: Optional[List[str]] = Field(None, description="List of treatment steps")
    severity: Optional[str] = Field(None, description="Severity: low, medium or high")
    error: Optional[str] = Field(None, description="Error message if not a plant")