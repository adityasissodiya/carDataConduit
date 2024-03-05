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
     # Define the filename where JSON data will be stored
    filename = "service_entries.json"
    
    # Prepare the data to write, including a timestamp for when the request was received
    data_to_write = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    }
    
    # Write the data to a file, appending to the file if it already exists
    with open(filename, "a") as file:
        json.dump(data_to_write, file)
        file.write("\n")  # Ensure each entry is on a new line

    return jsonify({"message": "Service entry added successfully"}), 201
