from flask import Flask
from neo4j import GraphDatabase
import os

app = Flask(__name__)

# Set up Neo4j connection
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(user, password))

@app.route('/')
def home():
    return "Welcome to the Car Rental API"

from app import routes
