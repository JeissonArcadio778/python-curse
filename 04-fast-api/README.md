# What is FastAPI? 

Is a modern framework for create APIs with Python. 

# Notes: 

# Generate .gitignore file 
gitignore.io
# Create virtual environment
python -m venv venv
# Activate virtual environment
source venv/bin/activate
# Deactivate virtual environment
deactivate
# Generate requirements.txt
pip freeze > requirements.txt
# Install requirements
pip install -r requirements.txt

# Run

python3 -m venv venv

source venv/bin/activate

pip install fastapi

pip install uvicorn

- Its like a nodemon: 
uvicorn main:app --reload --port 5000


# Automatic documentation with Swagger: 

http://127.0.0.1:5000/docs