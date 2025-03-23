import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD

# 📌 Email Alert Function
def send_email_alert(missing_items, room_id):
    if not missing_items:
        return  

    msg = EmailMessage()
    msg['Subject'] = f"🚨 Missing Items Alert for Room {room_id}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = "manager_email@gmail.com"  # Replace with actual email
    msg.set_content(f"Missing items detected: {', '.join(missing_items)}.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# 📌 IoT Automation Function
def smart_home_action(missing_items):
    if "door key" in missing_items:
        return "🔐 Door key missing! Locking smart doors for security."
    elif "fire extinguisher" in missing_items:
        return "🔥 EMERGENCY! Fire extinguisher is missing! Alerting security."
    return "No emergency actions needed."
