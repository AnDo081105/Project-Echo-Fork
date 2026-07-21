# MongoDB with FastAPI

Owner: Backend.

Status: prototype API moved from `src/prototypes/api/FastAPI` to `src/prototypes/api/api`.

This is a prototype demonstrating how to connect FastAPI with the MongoDB database and make some queries. The canonical production API remains `src/Components/API`.


# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
set the variable in app.py client = pymongo.MongoClient("mongodb://localhost:27017") or whatever other connection string you have set up.

# Start the service:

open conda shell and cd to the api folder, then run:

python -m uvicorn app:app --reload

Head to localhost:8000/docs to read the documentation for API
