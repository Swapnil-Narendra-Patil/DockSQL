# Import necessary libraries
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set Postgres database configuration
POSTGRES_HOST = "postgres"
POSTGRES_PORT = "5432"
POSTGRES_USER = "process_trending"
POSTGRES_PASSWORD = "abc123"
POSTGRES_DB = "brx1"
PGDATA = "/var/lib/postgresql/data/pgdata"

# Create Postgres URL string
url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Set database URI configuration for Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = url

# Initialize database connection
db = SQLAlchemy(app)

# Create SQLAlchemy model for TempValue table
class TempValue(db.Model):
    __tablename__ = 'CM_HAM_DO_AI1/Temp_value'
    time = db.Column(db.Date, primary_key=True)
    value = db.Column(db.Float)

# Define route for home page
@app.get("/")
def home():
    # Query all TempValue entries from database
    temp_values = TempValue.query.all()
    # Convert query results to JSON format and return as response
    return jsonify([{'Temp_value': temp.value} for temp in temp_values])

# Start Flask app if this script is run as main program
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5400)