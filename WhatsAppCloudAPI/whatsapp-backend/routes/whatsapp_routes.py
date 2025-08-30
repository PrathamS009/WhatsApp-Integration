from flask import Blueprint, request, jsonify
from controllers.whatsapp_controller import send_whatsapp_message

whatsapp_bp=Blueprint("whatsapp_bp",__name__)

@whatsapp_bp.route("/send", methods=['POST'])
def send_message():
    data=request.json
    number=data.get("number")
    message=data.get("message")
    
    if not number or not message:
        return jsonify({"ERROR":"Number and Message is required"}), 400
    
    result=send_whatsapp_message(number, message)
    
    return jsonify(result)