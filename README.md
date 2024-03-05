### Application Structure

The Flask application is structured into several key components:

- `app/__init__.py`: Initializes the Flask app and registers blueprints.
- `app/models.py`: Contains the RDF model and functions for interacting with the RDF graph, including adding service entries.
- `app/views.py`: Defines the API endpoints, including the secured endpoint for adding service entries.
- `app/auth.py`: Implements the simple token-based authentication and ABAC policy checks.

### Key Features

- **Simple Token-Based Authentication**: A basic authentication mechanism that uses pre-defined tokens to authenticate API requests.
- **Attribute-Based Access Control (ABAC)**: Ensures that only authorized entities, such as certified workshops, can perform specific actions (e.g., adding service entries).

### Setting Up the Project

1. Install required Python packages from `requirements.txt` using pip:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application locally:

    ```bash
    flask run
    ```

### Testing the API

To test the `/add_service_entry` API endpoint with Postman:

1. **Configure the Request:**
    - Set the request method to `POST`.
    - Use the endpoint URL: `http://localhost:5000/add_service_entry`.
    - Add a header: `Content-Type` set to `application/json`.
    - Add an authorization header: `Authorization` with the value set to one of the pre-defined tokens.

2. **Set the Request Body:**
    - Choose `raw` and format `JSON`, then input your data, for example:

        ```json
        {
          "vin": "VIN12345XYZ",
          "service_date": "2023-09-01",
          "service_detail": "Oil change and tire rotation."
        }
        ```

3. **Send the Request:**
    - Click `Send` and observe the response.

### Authentication Tokens

Use one of the pre-defined tokens in the `Authorization` header to authenticate. For testing, the token `"certified_workshop_token"` can be used to simulate a request from a certified workshop. Ensure that the token you use matches one of those defined in `app/auth.py`.

### Important Considerations

- This project uses a simplified authentication system for demonstration purposes. For production environments, consider using a more robust authentication mechanism.
- The application's ABAC system is designed to demonstrate basic access control. Adjust the access control policies in `app/auth.py` according to your specific requirements.