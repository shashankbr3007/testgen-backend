from fastapi import APIRouter, Depends
from app.models.test_case_model import TestGenRequest
from app.services.test_case_generator import TestCaseGenerator

router = APIRouter()


@router.post("/generate")
async def generate_testcases(payload: TestGenRequest):
    testcases = await TestCaseGenerator.generate(payload)
    return {"count": len(testcases), "testcases": testcases}
