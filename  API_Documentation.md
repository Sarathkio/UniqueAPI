# **API Documentation**

### API Endpoints

**/api/data/ (GET Request)**
* Description: Retrieves all data objects from the database.
* Request Method: GET
* Request Payload: No payload required
* Response Format:
* Content-Type: application/json
* Example Response:
[
    {
        "id": 1,
        "name": "John",
        "age": 25,
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    },
    ...
]

**/api/merge/ (POST Request)**
* Description: Merges data objects into the database.
* Request Method: POST
* Request Payload Format:
* Content-Type: application/json
* Example Request Payload:

[
    {
        "name": "John",
        "age": 25,
        "email": "john@example.com"
    },
    {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    },
    ...
]

**Response Format:**
Content-Type: application/json
Example Response (Success):
{
    "status": "success",
    "message": "Data objects merged successfully"
}
**Example Response (Error):**
{
    "status": "error",
    "message": "Validation error: 'age' field must be a positive integer"
}


**Project Setup Instructions**

1. Clone the project repository from GitHub.
2. Install Python (if not already installed).
3. Install Django and psycopg2 using pip.
4. Set up PostgreSQL database and configure the database settings in settings.py.
5. Run database migrations using python manage.py migrate.
6. Start the Django development server using python manage.py runserver.

**Executing the Endpoints**

1. Open a web browser or use a REST client like Postman.
2. Send GET requests to /api/data/ to retrieve data objects.
3. Send POST requests to /api/merge/ with valid JSON payload to merge data objects into the database.
4. Database Configuration and psycopg2 Usage
5. Configure PostgreSQL database settings in settings.py under the DATABASES dictionary.
6. Install psycopg2 using pip (pip install psycopg2) to enable PostgreSQL integration.
7. Utilize psycopg2 for database interactions in Django views or serializers.