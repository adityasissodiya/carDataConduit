from flask import Blueprint, request, jsonify
from .auth import get_user_attributes, is_authorized
from .models import add_service_entry

app = Blueprint('views', __name__)

@app.route('/add_service_entry', methods=['POST'])
def api_add_service_entry():
    token = request.headers.get("Authorization")
    user_attributes = get_user_attributes(token)
    
    if not user_attributes or not is_authorized(user_attributes, "write"):
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.json
    # Extract and validate data from request.json
    # Call add_service_entry(...) with the validated data
    return jsonify({"message": "Service entry added successfully"}), 201
