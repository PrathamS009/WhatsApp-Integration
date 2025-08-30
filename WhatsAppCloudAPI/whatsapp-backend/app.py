from flask import Flask
from flask_cors import CORS
from routes.whatsapp_routes import whatsapp_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(whatsapp_bp, url_prefix="/api/whatsapp")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
