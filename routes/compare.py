from fastapi import APIRouter
from database import session, RoomScan
from actions import chatbot_response, send_email_alert, smart_home_action

router = APIRouter()

@router.get("/compare/{room_id}")
def compare_images(room_id: str):
    room_scan = session.query(RoomScan).filter(RoomScan.room_id == room_id).first()
    
    if not room_scan:
        return {"error": "Room scan not found"}
    
    missing_items = set(room_scan.before_items) - set(room_scan.after_items)
    
    chatbot_message = chatbot_response(missing_items)
    send_email_alert(missing_items, room_id)
    iot_action = smart_home_action(missing_items)
    
    return {"room_id": room_id, "missing_items": list(missing_items), "chatbot": chatbot_message, "iot_action": iot_action}


