from pydantic import BaseModel
from typing import List

class TestGenRequest(BaseModel):
    requirements: str | None = None
    personas: str | None = None
    business_process: str | None = None
    customer_journey: str | None = None
    site_content: str | None = None

class TestCase(BaseModel):
    test_name: str
    description: str
    steps: List[str]
    expected: str
    actual: str
    status: str
