To set up a Flask application with MongoDB, you need to perform a series of steps in the terminal. Here are the necessary Bash commands:


# Step 1: Set up a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Step 2: Install Flask and PyMongo
pip install Flask pymongo

# Step 3: Ensure MongoDB is installed and running
# Instructions differ per OS
Windows :- Download the MongoDB installer from the official MongoDB website, then follow the installation instructions.
Ubuntu:- bash code was below--
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb

# Step 4: Run MongoDB server
mongod &  # Use '&' to run it in the background

# Step 5: Run Flask application
python app.py

