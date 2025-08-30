from flask import Blueprint, request, jsonify
from controllers.whatsapp_controller import send_whatsapp_message

whatsapp_bp=Blueprint("whatsapp_bp",__name__)

@whatsapp_bp.route("/send", methods=['POST'])
def send_message():
    data = request.json
    number = data.get("number")
    message = data.get("message")
    
    if not number or not message:
        return jsonify({"status": "error", "message": "Number and Message are required"}), 400
    
    result = send_whatsapp_message(number, message)
    
    if "error" in result:
        if result["error"].get("code") == 131030:
            return jsonify({"status": "error", "message": "Number not listed"}), 400
        else:
            return jsonify({"status": "error", "message": "Error sending message"}), 500

    return jsonify({"status": "success", "message": "Message sent successfully"})
