from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}
