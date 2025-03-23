from fastapi import APIRouter, UploadFile, File
import shutil
from detection import detect_items
from database import save_scan

router = APIRouter()

@router.post("/upload/before/{room_id}")
async def upload_before(room_id: str, file: UploadFile = File(...)):
    image_path = f"static/before_{room_id}.jpg"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    detected_items = detect_items(image_path)
    save_scan(room_id, before_items=detected_items)

    return {"room_id": room_id, "detected_items": detected_items}

@router.post("/upload/after/{room_id}")
async def upload_after(room_id: str, file: UploadFile = File(...)):
    image_path = f"static/after_{room_id}.jpg"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detected_items = detect_items(image_path)
    return {"room_id": room_id, "detected_items": detected_items}
